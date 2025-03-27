import openpyxl
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QDateEdit, QPushButton, QTableWidget, QLabel
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIcon
from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.ui.BillSummary import Ui_MainWindow


class BillSummaryEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()  # Kết nối với cơ sở dữ liệu
        self.bills = []  # Danh sách các bill
        self.total_revenue = 0  # Tổng doanh thu

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self._setup_table_columns()  # Cấu hình bảng
        self._link_ui_components()  # Liên kết các thành phần UI
        self.Signal()  # Kết nối các sự kiện
        self.load_bills()  # Tải danh sách bill ban đầu

    def _link_ui_components(self):
        """Liên kết các thành phần UI và kiểm tra giá trị None"""
        try:
            # Liên kết các QDateEdit và QPushButton
            self.dateEditFrom = self.MainWindow.findChild(QDateEdit, "dateEditFrom")
            self.dateEditTo = self.MainWindow.findChild(QDateEdit, "dateEditTo")
            self.pushButtonLoc = self.MainWindow.findChild(QPushButton, "pushButtonLoc")
            self.pushButtonExport = self.MainWindow.findChild(QPushButton, "pushButtonExport")
            self.pushButtonTinhDoanhThu = self.MainWindow.findChild(QPushButton, "pushButtonTinhDoanhThu")
            self.pushButtonXemChiTiet = self.MainWindow.findChild(QPushButton, "pushButtonXemChiTiet")
            self.pushButtonClose = self.MainWindow.findChild(QPushButton, "pushButtonClose")

            # Liên kết QTableWidget và QLabel
            self.tableWidgetDanhSachBill = self.MainWindow.findChild(QTableWidget, "tableWidgetDanhSachBill")
            self.labelTienDoanhThu = self.MainWindow.findChild(QLabel, "labelTienDoanhThu")
            # Cấu hình QDateEdit
            self.dateEditFrom.setCalendarPopup(True)  # Bật lịch popup
            self.dateEditFrom.setDisplayFormat("yyyy-MM-dd")  # Định dạng ngày
            self.dateEditFrom.setDate(QDate.currentDate().addMonths(-1))

            self.dateEditTo.setCalendarPopup(True)  # Bật lịch popup
            self.dateEditTo.setDisplayFormat("yyyy-MM-dd")  # Định dạng ngày
            self.dateEditTo.setDate(QDate.currentDate())
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi liên kết UI: {str(e)}")
            raise

    def _setup_table_columns(self):
        self.tableWidgetDanhSachBill.setColumnCount(4)
        self.tableWidgetDanhSachBill.setHorizontalHeaderLabels(["Mã Bill", "Ngày tạo", "Tổng tiền", "Trạng thái"])
        self.tableWidgetDanhSachBill.setColumnWidth(0, 100)
        self.tableWidgetDanhSachBill.setColumnWidth(1, 150)
        self.tableWidgetDanhSachBill.setColumnWidth(2, 150)
        self.tableWidgetDanhSachBill.setColumnWidth(3, 100)

    def Signal(self):
        """Kết nối các sự kiện với các phương thức xử lý"""
        self.pushButtonLoc.clicked.connect(self.filter_bills)
        self.pushButtonTinhDoanhThu.clicked.connect(self.calculate_revenue)
        self.pushButtonXemChiTiet.clicked.connect(self.view_bill_details)
        self.pushButtonExport.clicked.connect(self.export_bills)
        self.pushButtonClose.clicked.connect(self.close_window)

    def load_bills(self):
        try:
            self.bills = self.dc.get_all_bills()
            self.display_bills(self.bills)
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải danh sách bill: {str(e)}")

    def display_bills(self, bills):
        self.tableWidgetDanhSachBill.setRowCount(0)
        self.bills=bills
        for bill in bills:
            row = self.tableWidgetDanhSachBill.rowCount()
            self.tableWidgetDanhSachBill.insertRow(row)
            self.tableWidgetDanhSachBill.setItem(row, 0, QTableWidgetItem(bill["bill_id"]))
            self.tableWidgetDanhSachBill.setItem(row, 1, QTableWidgetItem(bill["date_created"]))
            self.tableWidgetDanhSachBill.setItem(row, 2, QTableWidgetItem(f"{bill['total_amount']:,.2f} VND"))
            self.tableWidgetDanhSachBill.setItem(row, 3, QTableWidgetItem(bill["status"]))
    def filter_bills(self):
        """Lọc bill theo khoảng thời gian"""
        try:
            from_date = self.dateEditFrom.date().toString("yyyy-MM-dd")
            to_date = self.dateEditTo.date().toString("yyyy-MM-dd")
            self.bills = self.dc.get_bills_by_date_range(from_date, to_date)
            self.display_bills(self.bills)
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể lọc bill: {str(e)}")

    def calculate_revenue(self):
        try:
            if not self.bills:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Không có bill nào để tính doanh thu!")
                self.labelTienDoanhThu.setText("Tổng doanh thu: 0 VND")
                return
            # Kiểm tra và chuyển đổi total_amount thành float nếu cần
            valid_bills = []
            for bill in self.bills:
                try:
                    bill["total_amount"] = float(bill["total_amount"])
                    valid_bills.append(bill)
                except (ValueError, TypeError):
                    print(f"Invalid total_amount in bill {bill['bill_id']}: {bill['total_amount']}")
                    continue
            if not valid_bills:
                raise ValueError("Không có bill nào có tổng tiền hợp lệ!")
            self.total_revenue = sum(bill["total_amount"] for bill in valid_bills)
            self.labelTienDoanhThu.setText(f"Tổng doanh thu: {self.total_revenue:,.2f} VND")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tính doanh thu: {str(e)}")
    def view_bill_details(self):
        try:
            selected_row = self.tableWidgetDanhSachBill.currentRow()
            if selected_row < 0:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn một bill để xem chi tiết!")
                return

            bill_id = self.tableWidgetDanhSachBill.item(selected_row, 0).text()
            bill_details = self.dc.get_bill_details(bill_id)
            details_message = "Chi tiết bill:\n" + "\n".join([f"{item['product_name']}: {item['quantity']} x {item['price']:,.2f} VND" for item in bill_details])
            QMessageBox.information(self.MainWindow, f"Chi tiết Bill {bill_id}", details_message)
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xem chi tiết bill: {str(e)}")

    def export_bills(self):
        try:
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = "DanhSachBill"
            headers = ["Mã Bill", "Ngày tạo", "Tổng tiền", "Trạng thái"]
            ws.append(headers)
            for row in range(self.tableWidgetDanhSachBill.rowCount()):
                row_data = [self.tableWidgetDanhSachBill.item(row, col).text() for col in range(4)]
                ws.append(row_data)
            wb.save("/Users/admin/Documents/python/K24406H/DoAnCuoiKy/dataset/DanhSachBill.xlsx")
            QMessageBox.information(self.MainWindow, "Thông báo", "Xuất file Excel thành công!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xuất file: {str(e)}")

    def close_window(self):
        """Đóng cửa sổ"""
        self.MainWindow.close()

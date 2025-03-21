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

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi liên kết UI: {str(e)}")
            raise

    def _setup_table_columns(self):
        """Cấu hình số cột và tiêu đề cho bảng"""
        self.tableWidgetDanhSachBill.setColumnCount(4)
        self.tableWidgetDanhSachBill.setHorizontalHeaderLabels([
            "Mã Bill", "Ngày tạo", "Tổng tiền", "Trạng thái"
        ])

    def Signal(self):
        """Kết nối các sự kiện với các phương thức xử lý"""
        self.pushButtonLoc.clicked.connect(self.filter_bills)
        self.pushButtonTinhDoanhThu.clicked.connect(self.calculate_revenue)
        self.pushButtonXemChiTiet.clicked.connect(self.view_bill_details)
        self.pushButtonExport.clicked.connect(self.export_bills)
        self.pushButtonClose.clicked.connect(self.close_window)

    def load_bills(self):
        """Tải danh sách bill từ DataConnector và hiển thị"""
        try:
            self.bills = self.dc.get_all_bills()
            self.tableWidgetDanhSachBill.setRowCount(0)

            for bill in self.bills:
                row = self.tableWidgetDanhSachBill.rowCount()
                self.tableWidgetDanhSachBill.insertRow(row)

                # Hiển thị thông tin bill
                self.tableWidgetDanhSachBill.setItem(row, 0, QTableWidgetItem(bill["bill_id"]))
                self.tableWidgetDanhSachBill.setItem(row, 1, QTableWidgetItem(bill["date_created"]))
                self.tableWidgetDanhSachBill.setItem(row, 2, QTableWidgetItem(f"{bill['total_amount']:,.2f} VND"))
                self.tableWidgetDanhSachBill.setItem(row, 3, QTableWidgetItem(bill["status"]))
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải danh sách bill: {str(e)}")

    def filter_bills(self):
        """Lọc bill theo khoảng thời gian"""
        try:
            from_date = self.dateEditFrom.date().toString("yyyy-MM-dd")
            to_date = self.dateEditTo.date().toString("yyyy-MM-dd")

            # Lọc bill từ cơ sở dữ liệu
            filtered_bills = self.dc.get_bills_by_date_range(from_date, to_date)
            self.tableWidgetDanhSachBill.setRowCount(0)  # Xóa toàn bộ hàng cũ

            for bill in filtered_bills:
                row = self.tableWidgetDanhSachBill.rowCount()
                self.tableWidgetDanhSachBill.insertRow(row)

                # Thêm dữ liệu vào các cột
                self.tableWidgetDanhSachBill.setItem(row, 0, QTableWidgetItem(bill.bill_id))
                self.tableWidgetDanhSachBill.setItem(row, 1, QTableWidgetItem(bill.date_created))
                self.tableWidgetDanhSachBill.setItem(row, 2, QTableWidgetItem(f"{bill.total_amount:,.2f} VND"))
                self.tableWidgetDanhSachBill.setItem(row, 3, QTableWidgetItem(bill.status))

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể lọc bill: {str(e)}")

    def calculate_revenue(self):
        """Tính tổng doanh thu từ các bill"""
        try:
            self.total_revenue = sum(bill.total_amount for bill in self.bills)
            self.labelTienDoanhThu.setText(f"{self.total_revenue:,.2f} VND")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tính doanh thu: {str(e)}")

    def view_bill_details(self):
        """Xem chi tiết bill được chọn"""
        try:
            selected_row = self.tableWidgetDanhSachBill.currentRow()
            if selected_row < 0:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn một bill để xem chi tiết!")
                return

            bill_id = self.tableWidgetDanhSachBill.item(selected_row, 0).text()
            bill_details = self.dc.get_bill_details(bill_id)  # Giả sử có phương thức get_bill_details trong DataConnector

            # Hiển thị chi tiết bill (ví dụ: trong một QMessageBox hoặc cửa sổ mới)
            details_message = "\n".join([f"{item.product_name}: {item.quantity} x {item.price:,.2f} VND" for item in bill_details])
            QMessageBox.information(self.MainWindow, "Chi tiết Bill", details_message)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xem chi tiết bill: {str(e)}")

    def export_bills(self):
        """Xuất danh sách bill ra file Word/PDF"""
        try:
            # Giả sử sử dụng thư viện python-docx để xuất file Word
            from docx import Document
            document = Document()
            document.add_heading('Danh sách Bill', 0)

            # Thêm dữ liệu từ bảng vào file Word
            table = document.add_table(rows=1, cols=4)
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Mã Bill'
            hdr_cells[1].text = 'Ngày tạo'
            hdr_cells[2].text = 'Tổng tiền'
            hdr_cells[3].text = 'Trạng thái'

            for row in range(self.tableWidgetDanhSachBill.rowCount()):
                row_cells = table.add_row().cells
                for col in range(4):
                    row_cells[col].text = self.tableWidgetDanhSachBill.item(row, col).text()

            # Lưu file
            document.save('DanhSachBill.docx')
            QMessageBox.information(self.MainWindow, "Thông báo", "Xuất file thành công!")

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xuất file: {str(e)}")

    def close_window(self):
        """Đóng cửa sổ"""
        self.MainWindow.close()
import sys

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLabel, QLineEdit, QTableWidget, QTableWidgetItem

from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow



class InventoryMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.products = []
        self.total_quantity = 0


    def setupUi(self, MainWindow):
        try:
            super().setupUi(MainWindow)
            self.MainWindow = MainWindow
            self._setup_table_columns()  # Cấu hình bảng
            # Liên kết các widget từ file UI
            self._link_ui_components()
            self.Signal()
        except Exception as e:
            QMessageBox.critical(None, "Lỗi khởi tạo", f"Không thể khởi tạo UI: {str(e)}")
            sys.exit(1)  # Thoát chương trình nếu lỗi nghiêm trọng

    def _link_ui_components(self):
        """Liên kết tất cả widget từ UI và kiểm tra giá trị None"""
        try:
            # Liên kết các QLineEdit
            self.lineEditProID = self.MainWindow.findChild(QLineEdit, "lineEditProID")
            self.lineEditProName = self.MainWindow.findChild(QLineEdit, "lineEditProName")
            self.lineEditPrice = self.MainWindow.findChild(QLineEdit, "lineEditPrice")
            self.lineEditQuantity = self.MainWindow.findChild(QLineEdit, "lineEditQuantity")
            self.lineEditCateID = self.MainWindow.findChild(QLineEdit, "lineEditCateID")

            # Liên kết QTableWidget và QLabel
            self.tableWidgetProduct = self.MainWindow.findChild(QTableWidget, "tableWidgetProduct")


            # Kiểm tra xem tất cả widget có tồn tại không
            if not all([
                self.lineEditProID, self.lineEditProName, self.lineEditPrice,
                self.lineEditQuantity, self.lineEditCateID, self.tableWidgetProduct,

            ]):
                missing = [name for name, widget in [
                    ("lineEditProID", self.lineEditProID),
                    ("lineEditProName", self.lineEditProName),
                    ("lineEditPrice", self.lineEditPrice),
                    ("lineEditQuantity", self.lineEditQuantity),
                    ("lineEditCateID", self.lineEditCateID),
                    ("tableWidgetProduct", self.tableWidgetProduct),

                ] if widget is None]

                error_msg = f"Thiếu các widget: {', '.join(missing)} trong UI!"
                QMessageBox.critical(self.MainWindow, "Lỗi UI", error_msg)
                raise RuntimeError(error_msg)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi liên kết UI: {str(e)}")
            raise
    def showWindow(self):
        self.MainWindow.show()
    def Signal(self):
        self.pushButtonCloseInventory.clicked.connect(self.back_SalesWindow)
        self.pushButtonNew.clicked.connect(self.xuly_moi)
        self.pushButtonAddProduct.clicked.connect(self.xuly_them)
        self.pushButtonRemoveProduct.clicked.connect(self.xuly_xoa)
    def back_SalesWindow(self):
        from DoAnCuoiKy.ui.SalesMainWindowEx import SalesMainWindowEx
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = SalesMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def xuly_moi(self):
        print("Xử lý tạo mới sản phẩm")
        self.lineEditProID.clear()
        self.lineEditProName.clear()
        self.lineEditPrice.clear()
        self.lineEditQuantity.clear()
        self.lineEditCateID.clear()

    def xuly_them(self):
        try:
            # Kiểm tra xem các widget đã được liên kết chưa
            if not hasattr(self, "tableWidgetProduct") or not self.tableWidgetProduct:
                raise AttributeError("Bảng sản phẩm chưa được liên kết")

            # Lấy dữ liệu từ các ô nhập
            product_id = self.lineEditProID.text().strip()
            product_name = self.lineEditProName.text().strip()
            product_price = self.lineEditPrice.text().strip()
            product_quantity = self.lineEditQuantity.text().strip()
            product_cate_id = self.lineEditCateID.text().strip()

            # Kiểm tra dữ liệu trống
            if not all([product_id, product_name, product_price, product_quantity, product_cate_id]):
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
                return

            # Kiểm tra định dạng số
            try:
                product_price = float(product_price)
                product_quantity = int(product_quantity)
            except ValueError:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Giá/số lượng không hợp lệ!")
                return

            # Thêm dữ liệu vào bảng
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
            self.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(product_id))
            self.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(product_name))
            self.tableWidgetProduct.setItem(row, 2, QTableWidgetItem(f"{product_price:,.2f}"))
            self.tableWidgetProduct.setItem(row, 3, QTableWidgetItem(str(product_quantity)))
            self.tableWidgetProduct.setItem(row, 4, QTableWidgetItem(product_cate_id))

            # Cập nhật tổng số lượng
            self.total_quantity += product_quantity
          

            # Xóa form nhập liệu
            self.xuly_moi()

        except Exception as e:
            QMessageBox.critical(
                self.MainWindow,
                "Lỗi hệ thống",
                f"Không thể thêm sản phẩm! Chi tiết: {str(e)}"
            )

    def xuly_xoa(self):
        try:
            selected_row = self.tableWidgetProduct.currentRow()
            if selected_row >= 0:
                 # Cập nhật tổng số lượng
                quantity = int(self.tableWidgetProduct.item(selected_row, 3).text())
                self.total_quantity -= quantity


                # Xóa hàng
                self.tableWidgetProduct.removeRow(selected_row)
            else:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn sản phẩm cần xóa!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi hệ thống: {str(e)}")

    def _setup_table_columns(self):
        """Cấu hình số cột và tiêu đề cho bảng"""
        self.tableWidgetProduct.setColumnCount(5)
        self.tableWidgetProduct.setHorizontalHeaderLabels([
            "Mã SP", "Tên SP", "Giá", "Số lượng", "Mã danh mục"
        ])
        # Đặt độ rộng cột (tuỳ chỉnh)
        self.tableWidgetProduct.setColumnWidth(0, 100)
        self.tableWidgetProduct.setColumnWidth(1, 200)
        self.tableWidgetProduct.setColumnWidth(2, 150)
        self.tableWidgetProduct.setColumnWidth(3, 100)
        self.tableWidgetProduct.setColumnWidth(4, 150)
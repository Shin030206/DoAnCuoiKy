from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLabel, QLineEdit, QTableWidget, QTableWidgetItem

from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow



class InventoryMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.labelTotalQuantity = None
        self.products=[]
        self.total_quantity=0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.Signal()
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
            product_id = self.lineEditProID.text()
            product_name = self.lineEditProName.text()
            product_price = self.lineEditPrice.text()
            product_quantity = self.lineEditQuantity.text()
            product_cate_id = self.lineEditCateID.text()

            # Kiểm tra dữ liệu hợp lệ
            if not all([product_id, product_name, product_price, product_quantity]):
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
                return

            # Chuyển đổi kiểu dữ liệu số
            try:
                product_price = float(product_price)
                product_quantity = int(product_quantity)
            except ValueError:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Giá hoặc số lượng không hợp lệ!")
                return

            # Thêm dữ liệu vào bảng
            row_position = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row_position)

            self.tableWidgetProduct.setItem(row_position, 0, QTableWidgetItem(product_id))
            self.tableWidgetProduct.setItem(row_position, 1, QTableWidgetItem(product_name))
            self.tableWidgetProduct.setItem(row_position, 2, QTableWidgetItem(f"{product_price:,.2f}"))
            self.tableWidgetProduct.setItem(row_position, 3, QTableWidgetItem(str(product_quantity)))
            self.tableWidgetProduct.setItem(row_position, 4, QTableWidgetItem(product_cate_id))

            # Cập nhật tổng số lượng
            self.total_quantity += product_quantity
            self.labelTotalQuantity.setText(f"Tổng số lượng: {self.total_quantity}")

            # Xóa các ô nhập liệu
            self.xuly_moi()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi hệ thống: {str(e)}")

    def xuly_xoa(self):
        try:
            selected_row = self.tableWidgetProduct.currentRow()
            if selected_row >= 0:
                 # Cập nhật tổng số lượng
                quantity = int(self.tableWidgetProduct.item(selected_row, 3).text())
                self.total_quantity -= quantity
                self.labelTotalQuantity.setText(f"Tổng số lượng: {self.total_quantity}")

                # Xóa hàng
                self.tableWidgetProduct.removeRow(selected_row)
            else:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn sản phẩm cần xóa!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi hệ thống: {str(e)}")

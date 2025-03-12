from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLabel, QLineEdit, QTableWidget

from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow



class InventoryMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
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

    def xuly_them(self):
        product_id = self.lineEditProID.text()
        product_name = self.lineEditProName.text()
        product_price = self.lineEditPrice.text()
        product_quantity = self.lineEditQuantity.text()

        if product_id and product_name and product_price and product_quantity:
            print(f"Thêm sản phẩm: {product_name}, Mã: {product_id}, Giá: {product_price}, Số lượng: {product_quantity}")
        else:
            print("Vui lòng điền đầy đủ thông tin sản phẩm")

    def xuly_xoa(self):
        selected_row = self.tableWidgetProduct.currentRow()

        if selected_row >= 0:
            print(f"Xóa sản phẩm tại hàng {selected_row}")
        else:
            print("Không có sản phẩm nào được chọn để xóa")

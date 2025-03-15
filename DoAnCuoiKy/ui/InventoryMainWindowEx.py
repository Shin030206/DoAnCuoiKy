from PyQt6.QtWidgets import QMainWindow

from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow



class InventoryMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.categories=self.dc.get_all_categories()
        self.products=self.dc.get_all_products()
        self.selected_cate = None
        self.selected_product = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.Signal()
    def showWindow(self):
        self.MainWindow.show()
    def Signal(self):
        self.pushButtonCloseInventory.clicked.connect(self.back_SalesWindow)
    def back_SalesWindow(self):
        from DoAnCuoiKy.ui.SalesMainWindowEx import SalesMainWindowEx
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = SalesMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    def detail_product(self):
        # get current selected index
        row = self.tableWidgetProduct.currentRow()
        if row < 0:  # not found selected index
            return
        self.selected_product = self.products[row]
        self.lineEditProID.setText(self.selected_product.proid)
        self.lineEditProName.setText(self.selected_product.proname)
        self.lineEditPrice.setText(str(self.selected_product.price))
        self.lineEditQuantity.setText(str(self.selected_product.quantity))
        self.lineEditCateID.setText(str(self.selected_product.cateid))
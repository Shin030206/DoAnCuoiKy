from PyQt6.QtWidgets import QMainWindow


from DoAnCuoiKy.ui.SalesMainWindow import Ui_MainWindow


class SalesMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.Signal()
    def showWindow(self):
        self.MainWindow.show()
    def Signal(self):
        self.pushButtonInventory.clicked.connect(self.process_Inventory)
    def process_Inventory(self):
        from DoAnCuoiKy.ui.InventoryMainWindowEx import InventoryMainWindowEx
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = InventoryMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
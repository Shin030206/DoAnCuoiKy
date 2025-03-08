from PyQt6.QtWidgets import QMainWindow

from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow



class InventoryMainWindowEx(Ui_MainWindow):
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
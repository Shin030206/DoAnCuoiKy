from PyQt6.QtWidgets import QMessageBox, QMainWindow

from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.ui.LoginMainWindow import Ui_MainWindow
from DoAnCuoiKy.ui.SalesMainWindowEx import SalesMainWindowEx


class LoginMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.Signal()
    def showWindow(self):
        self.MainWindow.show()
    def Signal(self):
        self.pushButtonExit.clicked.connect(self.process_exit)
        self.pushButtonLogin.clicked.connect(self.process_login)
    def process_exit(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle('Xác nhận thoát')
        dlg.setText('Ê...Thoát thật hả?')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        if dlg.exec() == QMessageBox.StandardButton.Yes:
            exit()
    def process_login(self):
        dc = DataConnector()
        username = self.lineEditUserName.text().strip()
        password = self.lineEditPassword.text().strip()
        # Kiểm tra loại tài khoản dựa trên radio button
        user_role = None
        if self.radioButtonStaff.isChecked():
            user_role = "st"
        elif self.radioButtonManager.isChecked():
            user_role = "mg"
        if not user_role:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText('Vui lòng chọn loại tài khoản')
            self.msg.exec()
            return
        usr = dc.login(user_role,username, password)
        if usr !=None:
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = SalesMainWindowEx()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
            if usr=='st':
                self.myui.pushButtonInventory.setDisabled(True)
            else:
                self.myui.pushButtonInventory.setDisabled(False)
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText('Đăng nhập thất bại')
            self.msg.exec()
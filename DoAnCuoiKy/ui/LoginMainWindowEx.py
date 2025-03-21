import json
import os
import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.ui.LoginMainWindow import Ui_MainWindow
from DoAnCuoiKy.ui.SalesMainWindowEx import SalesMainWindowEx

class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        # Xác định đường dẫn tuyệt đối và tạo thư mục nếu cần
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../dataset"))
        print(f"Base directory: {self.base_dir}")
        if not os.path.exists(self.base_dir):
            try:
                os.makedirs(self.base_dir)
                print(f"Created directory: {self.base_dir}")
            except Exception as e:
                print(f"Failed to create directory {self.base_dir}: {str(e)}")
        self.login_file = os.path.join(self.base_dir, "login_info.json")
        print(f"Login file path: {self.login_file}")
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self._link_ui_components()
        self.Signal()
        self.load_saved_login()

    def _link_ui_components(self):
        try:
            self.lineEditUserName = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEditUserName")
            self.lineEditPassword = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEditPassword")
            self.checkBoxSavePassWord = self.MainWindow.findChild(QtWidgets.QCheckBox, "checkBoxSavePassWord")
            self.pushButtonExit = self.MainWindow.findChild(QtWidgets.QPushButton, "pushButtonExit")
            self.pushButtonLogin = self.MainWindow.findChild(QtWidgets.QPushButton, "pushButtonLogin")
            self.radioButtonStaff = self.MainWindow.findChild(QtWidgets.QRadioButton, "radioButtonStaff")
            self.radioButtonManager = self.MainWindow.findChild(QtWidgets.QRadioButton, "radioButtonManager")

            if not all([self.lineEditUserName, self.lineEditPassword, self.checkBoxSavePassWord,
                        self.pushButtonExit, self.pushButtonLogin, self.radioButtonStaff, self.radioButtonManager]):
                raise ValueError("Một hoặc nhiều thành phần UI không được tìm thấy trong file .ui!")
            print("UI components linked successfully")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi liên kết UI: {str(e)}")
            raise

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
            sys.exit()

    def process_login(self):
        username = self.lineEditUserName.text().strip()
        password = self.lineEditPassword.text().strip()

        user_role = None
        if self.radioButtonStaff.isChecked():
            user_role = "st"
        elif self.radioButtonManager.isChecked():
            user_role = "mg"

        if not user_role:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn loại tài khoản!")
            return

        if not username or not password:
            QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu!")
            return

        usr = self.dc.login(user_role, username, password)
        if usr:
            print(f"Login successful: {username}, role: {user_role}")
            self.save_login_info()  # Lưu thông tin đăng nhập trước khi chuyển giao diện
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = SalesMainWindowEx()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
            if usr == 'st':
                self.myui.pushButtonInventory.setDisabled(True)
            else:
                self.myui.pushButtonInventory.setDisabled(False)
        else:
            QMessageBox.critical(self.MainWindow, "Lỗi", "Đăng nhập thất bại! Tên đăng nhập hoặc mật khẩu không đúng.")

    def save_login_info(self):
        """Lưu thông tin đăng nhập nếu checkbox được chọn"""
        try:
            if self.checkBoxSavePassWord.isChecked():
                login_data = {
                    "username": self.lineEditUserName.text().strip(),
                    "password": self.lineEditPassword.text().strip(),
                    "save_password": True,
                    "user_role": "st" if self.radioButtonStaff.isChecked() else "mg"
                }
                print(f"Preparing to save login info: {login_data}")
            else:
                login_data = {"username": "", "password": "", "save_password": False, "user_role": ""}
                print("Checkbox not checked, resetting login info")

            # Ghi file và kiểm tra kết quả
            with open(self.login_file, 'w', encoding='utf-8') as f:
                json.dump(login_data, f, ensure_ascii=False, indent=4)
            if os.path.isfile(self.login_file):
                print(f"Login info successfully saved to: {self.login_file}")
            else:
                print(f"Failed to verify file creation at: {self.login_file}")
        except Exception as e:
            print(f"Error saving login info: {str(e)}")
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể lưu thông tin đăng nhập: {str(e)}")

    def load_saved_login(self):
        """Tải thông tin đăng nhập đã lưu và điền vào các QLineEdit"""
        try:
            if os.path.isfile(self.login_file):
                with open(self.login_file, 'r', encoding='utf-8') as f:
                    login_data = json.load(f)
                    print(f"Loaded login info: {login_data}")
                    if login_data.get("save_password", False):
                        self.lineEditUserName.setText(login_data.get("username", ""))
                        self.lineEditPassword.setText(login_data.get("password", ""))
                        self.checkBoxSavePassWord.setChecked(True)
                        if login_data.get("user_role") == "st":
                            self.radioButtonStaff.setChecked(True)
                        elif login_data.get("user_role") == "mg":
                            self.radioButtonManager.setChecked(True)
                    else:
                        self.checkBoxSavePassWord.setChecked(False)
            else:
                print(f"Login file does not exist at: {self.login_file}")
        except Exception as e:
            print(f"Error loading login info: {str(e)}")
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải thông tin đăng nhập: {str(e)}")
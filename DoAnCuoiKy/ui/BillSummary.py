# Form implementation generated from reading ui file 'D:\DoAnCuoiKy\DoAnCuoiKy\ui\BillSummary.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 826)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 851, 81))
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color:rgb(0,0,0);\n"
"    margin: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid #000000; /* Viền đen */\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 1001, 131))
        self.groupBox.setStyleSheet("background-color: #FAEED1;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(parent=self.groupBox)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 121))
        self.frame.setStyleSheet("QFrame {\n"
"   \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid #353924; /* Màu đỏ */\n"
"    border-radius: 10px;\n"
"    margin: 10px;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.dateEditFrom = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEditFrom.setGeometry(QtCore.QRect(109, 40, 121, 41))
        self.dateEditFrom.setStyleSheet("color: rgb(0, 0, 0);")
        self.dateEditFrom.setObjectName("dateEditFrom")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 101, 61))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 111, 61))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.dateEditTo = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEditTo.setGeometry(QtCore.QRect(340, 40, 131, 41))
        self.dateEditTo.setStyleSheet("color: rgb(0, 0, 0);")
        self.dateEditTo.setObjectName("dateEditTo")
        self.pushButtonLoc = QtWidgets.QPushButton(parent=self.frame)
        self.pushButtonLoc.setGeometry(QtCore.QRect(490, 40, 81, 41))
        self.pushButtonLoc.setStyleSheet("QPushButton {\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"                 background-color: #FEAE6F;\n"
"                 color:rgb(0,0,0);\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FEAE6F;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #AAB99A;\n"
"             }")
        self.pushButtonLoc.setObjectName("pushButtonLoc")
        self.pushButtonExport = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonExport.setGeometry(QtCore.QRect(600, 30, 381, 61))
        self.pushButtonExport.setStyleSheet("QPushButton {\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"                 background-color: #AAB99A;\n"
"                 color:rgb(0,0,0);\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #AAB99A;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #AAB99A;\n"
"             }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\DoAnCuoiKy\\DoAnCuoiKy\\ui\\../images/4373169_excel_logo_logos_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonExport.setIcon(icon)
        self.pushButtonExport.setIconSize(QtCore.QSize(40, 40))
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 230, 1001, 371))
        self.frame_2.setStyleSheet("\n"
"          QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.8);\n"
"              border: 2px solid #205781;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"          }\n"
"        \n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(100, 20, 811, 61))
        self.label_4.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.tableWidgetDanhSachBill = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidgetDanhSachBill.setGeometry(QtCore.QRect(30, 80, 941, 271))
        self.tableWidgetDanhSachBill.setStyleSheet("border-radius: 15px;\n"
"background-color: #D8D2C2;\n"
"color: rgb(0, 0, 0);")
        self.tableWidgetDanhSachBill.setObjectName("tableWidgetDanhSachBill")
        self.tableWidgetDanhSachBill.setColumnCount(4)
        self.tableWidgetDanhSachBill.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDanhSachBill.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDanhSachBill.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDanhSachBill.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDanhSachBill.setHorizontalHeaderItem(3, item)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 610, 961, 71))
        self.frame_3.setStyleSheet("background-color: #7E99A3;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 281, 61))
        self.label_5.setStyleSheet("\n"
"          QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.8);\n"
"              border: 2px solid #205781;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"          }\n"
"        \n"
"background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.labelTienDoanhThu = QtWidgets.QLabel(parent=self.frame_3)
        self.labelTienDoanhThu.setGeometry(QtCore.QRect(320, 10, 591, 41))
        self.labelTienDoanhThu.setStyleSheet("background-color: rgb(255, 255, 255);\n"
" font-size: 16px;\n"
" color: #AA0000;\n"
"  font-weight: bold;\n"
"   margin-left: 5px;\n"
"          ")
        self.labelTienDoanhThu.setObjectName("labelTienDoanhThu")
        self.pushButtonXemChiTiet = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonXemChiTiet.setGeometry(QtCore.QRect(410, 700, 211, 51))
        self.pushButtonXemChiTiet.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #FF6666;\n"
"                \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"                 color: black;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FF3333;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #CC0000;\n"
"             }\n"
"            ")
        self.pushButtonXemChiTiet.setObjectName("pushButtonXemChiTiet")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(700, 700, 231, 51))
        self.pushButtonClose.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #B7B7B7;\n"
"                \n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"                 color: black;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #B7B7B7;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #CC0000;\n"
"             }\n"
"            ")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\DoAnCuoiKy\\DoAnCuoiKy\\ui\\../../../Download/619539_close_delete_dismiss_exit_cancel_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonClose.setIcon(icon1)
        self.pushButtonClose.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.pushButtonTinhDoanhThu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonTinhDoanhThu.setGeometry(QtCore.QRect(110, 700, 211, 51))
        self.pushButtonTinhDoanhThu.setStyleSheet("QPushButton {\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"                 background-color: #FFAB5B;\n"
"                 color:rgb(0,0,0);\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FFAB5B;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #FFAB5B;\n"
"             }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\DoAnCuoiKy\\DoAnCuoiKy\\ui\\../../../Download/2530794_accounting_calculate_calculation_calculator_general_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonTinhDoanhThu.setIcon(icon2)
        self.pushButtonTinhDoanhThu.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonTinhDoanhThu.setObjectName("pushButtonTinhDoanhThu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Tổng hợp Bill</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Từ ngày"))
        self.label_3.setText(_translate("MainWindow", "Đến ngày:"))
        self.pushButtonLoc.setText(_translate("MainWindow", "Lọc"))
        self.pushButtonExport.setText(_translate("MainWindow", "Xuất Excel"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Danh sách Bill</span></p></body></html>"))
        item = self.tableWidgetDanhSachBill.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetDanhSachBill.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetDanhSachBill.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidgetDanhSachBill.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Tổng doanh thu</p></body></html>"))
        self.labelTienDoanhThu.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">0 VND</span></p></body></html>"))
        self.pushButtonXemChiTiet.setText(_translate("MainWindow", "Xem chi tiết"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
        self.pushButtonTinhDoanhThu.setText(_translate("MainWindow", "Tính doanh thu"))

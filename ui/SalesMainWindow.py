# Form implementation generated from reading ui file 'D:\Kĩ Thuật Lập Trình\ĐoAnCuoiKy\SalesMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1633, 911)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 371, 611))
        self.frame.setStyleSheet("  QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.8);\n"
"              border: 2px solid #FFD1BA;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"          }\n"
"         ")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 62, 28);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(parent=self.frame)
        self.listWidget.setStyleSheet("border-radius: 15px;\n"
"background-color: #F2F6D0;\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 961, 71))
        self.label_2.setStyleSheet("\n"
"        QLabel {\n"
"            font-size: 24px;\n"
"            font-weight: bold;\n"
"            color: #444444;\n"
"            margin: 10px;\n"
"            background-color: rgba(255,255,255,0.6);\n"
"            border-radius: 10px;\n"
"            padding: 5px 10px;\n"
"        }\n"
"       ")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(390, 80, 371, 611))
        self.frame_2.setStyleSheet("\n"
"          QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.8);\n"
"              border: 2px solid #FFD1BA;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"          }\n"
"         ")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 62, 28);\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidget.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(222, 254, 255);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(780, 80, 371, 611))
        self.frame_3.setStyleSheet("\n"
"          QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.9);\n"
"              border: 2px solid #FFAAAA;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"          }\n"
"         ")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 349, 71))
        self.label_4.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 62, 28);\n"
"")
        self.label_4.setObjectName("label_4")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.frame_3)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 70, 331, 271))
        self.listWidget_2.setStyleSheet("color: rgb(255, 237, 255);\n"
"background-color: #FFCFCF;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(30, 360, 311, 31))
        self.pushButton.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #FFAA88;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FF8866;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #FF6644;\n"
"             }\n"
"            ")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 410, 311, 31))
        self.pushButton_2.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #FFAA88;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FF8866;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #FF6644;\n"
"             }\n"
"            ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 460, 311, 31))
        self.pushButton_3.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #FFAA88;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FF8866;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #FF6644;\n"
"             }\n"
"            ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 510, 311, 31))
        self.pushButton_4.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #FFAA88;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #FF8866;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #FF6644;\n"
"             }\n"
"            ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 560, 311, 31))
        self.pushButton_5.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #CCBBFF;\n"
"                 color: black;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #9988FF;\n"
"                 color: white;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #7766DD;\n"
"             }\n"
"            ")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1633, 26))
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
        self.frame.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Danh mục</span></p></body></html>"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff220e;\">Danh mục </span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Danh mục</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Màn hình bán hàng</p></body></html>"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff220e;\">Danh mục </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sản phẩm</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff220e;\">Danh mục </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hóa đơn</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "New Sales"))
        self.pushButton_2.setText(_translate("MainWindow", "Add to Bill"))
        self.pushButton_3.setText(_translate("MainWindow", "Remove from Bill"))
        self.pushButton_4.setText(_translate("MainWindow", "Calculate (VAT 8%)"))
        self.pushButton_5.setText(_translate("MainWindow", "Go to Inventory"))

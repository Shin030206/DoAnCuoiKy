# Form implementation generated from reading ui file 'D:\Kĩ Thuật Lập Trình\ĐoAnCuoiKy\DoAnCuoiKy\DoAnCuoiKy\ui\SalesMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 761)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 80, 381, 611))
        self.frame.setStyleSheet("  QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.8);\n"
"              border: 2px solid #205781;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"          }\n"
"    color: rgb(255, 255, 255);\n"
"         ")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 1, 7);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidgetCategory = QtWidgets.QListWidget(parent=self.frame)
        self.listWidgetCategory.setStyleSheet("border-radius: 15px;\n"
"background-color: #DED0BA;\n"
"color: rgb(0, 0, 0);")
        self.listWidgetCategory.setObjectName("listWidgetCategory")
        self.verticalLayout.addWidget(self.listWidgetCategory)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 10, 961, 71))
        self.label_2.setStyleSheet("QLabel {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #444444;\n"
"    margin: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid black;  /* Thêm viền màu đen */\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(390, 80, 371, 611))
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 1, 7);\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidgetProduct = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidgetProduct.setStyleSheet("border-radius: 15px;\n"
"background-color: #DCE4B8;\n"
"color: rgb(0, 0, 0);")
        self.tableWidgetProduct.setObjectName("tableWidgetProduct")
        self.tableWidgetProduct.setColumnCount(3)
        self.tableWidgetProduct.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetProduct.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidgetProduct)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(760, 80, 371, 611))
        self.frame_3.setStyleSheet("\n"
"          QFrame {\n"
"              background-color: rgba(255, 255, 255, 0.9);\n"
"              border: 2px solid #205781;\n"
"              border-radius: 10px;\n"
"              margin: 10px;\n"
"          }\n"
"        \n"
"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 349, 71))
        self.label_4.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(252, 1, 7);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.listWidgetBill = QtWidgets.QListWidget(parent=self.frame_3)
        self.listWidgetBill.setGeometry(QtCore.QRect(20, 70, 331, 271))
        self.listWidgetBill.setStyleSheet("color: rgb(255, 237, 255);\n"
"background-color: #F4F2EF;")
        self.listWidgetBill.setObjectName("listWidgetBill")
        self.pushButtonNewSales = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonNewSales.setGeometry(QtCore.QRect(30, 360, 311, 31))
        self.pushButtonNewSales.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #CC7952;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #FF6644;\n"
"             }\n"
"            ")
        self.pushButtonNewSales.setObjectName("pushButtonNewSales")
        self.pushButtonAddBill = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonAddBill.setGeometry(QtCore.QRect(30, 410, 311, 31))
        self.pushButtonAddBill.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #CC7952;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"            ")
        self.pushButtonAddBill.setObjectName("pushButtonAddBill")
        self.pushButtonRemoveFromBill = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonRemoveFromBill.setGeometry(QtCore.QRect(30, 460, 311, 31))
        self.pushButtonRemoveFromBill.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #CC7952;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"            ")
        self.pushButtonRemoveFromBill.setObjectName("pushButtonRemoveFromBill")
        self.pushButtonCalculate = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(30, 510, 311, 31))
        self.pushButtonCalculate.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #CC7952;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"                 font-weight: bold;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #CC7952;\n"
"             }\n"
"            ")
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.pushButtonInventory = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonInventory.setGeometry(QtCore.QRect(30, 560, 311, 31))
        self.pushButtonInventory.setStyleSheet("\n"
"             QPushButton {\n"
"                 background-color: #213E60;\n"
"                 color: white;\n"
"                 border-radius: 5px;\n"
"                 padding: 8px;\n"
"             }\n"
"             QPushButton:hover {\n"
"                 background-color: #213E60;\n"
"                 color: white;\n"
"             }\n"
"             QPushButton:pressed {\n"
"                 background-color: #213E60\n"
"             }\n"
"            ")
        self.pushButtonInventory.setObjectName("pushButtonInventory")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1221, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sales_MainWindow"))
        self.frame.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Danh mục</span></p></body></html>"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff220e;\">Danh mục </span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Danh mục</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Màn hình bán hàng</p></body></html>"))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff220e;\">Danh mục </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sản phẩm</p></body></html>"))
        item = self.tableWidgetProduct.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetProduct.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetProduct.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff220e;\">Danh mục </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hóa đơn</p></body></html>"))
        self.pushButtonNewSales.setText(_translate("MainWindow", "New Sales"))
        self.pushButtonAddBill.setText(_translate("MainWindow", "Add to Bill"))
        self.pushButtonRemoveFromBill.setText(_translate("MainWindow", "Remove from Bill"))
        self.pushButtonCalculate.setText(_translate("MainWindow", "Calculate (VAT 8%)"))
        self.pushButtonInventory.setText(_translate("MainWindow", "Go to Inventory"))

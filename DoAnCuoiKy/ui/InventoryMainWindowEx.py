from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidget, QTableWidgetItem, QListWidgetItem, QListWidget, QPushButton
from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Product import Product
from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow

class InventoryMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.dc = DataConnector()
        self.categories = self.dc.get_all_categories()
        self.products = self.dc.get_all_products()
        self.total_quantity = 0
        self.selected_cate = None
        self.is_filtered = False
        self.last_filtered_cateid = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self._setup_table_columns()
        self._link_ui_components()
        self.Signal()
        self.load_products()
        self.load_categories()

    def _link_ui_components(self):
        try:
            self.lineEditProID = self.MainWindow.findChild(QLineEdit, "lineEditProID")
            self.lineEditProName = self.MainWindow.findChild(QLineEdit, "lineEditProName")
            self.lineEditPrice = self.MainWindow.findChild(QLineEdit, "lineEditPrice")
            self.lineEditQuantity = self.MainWindow.findChild(QLineEdit, "lineEditQuantity")
            self.lineEditCateID = self.MainWindow.findChild(QLineEdit, "lineEditCateID")
            self.tableWidgetProduct = self.MainWindow.findChild(QTableWidget, "tableWidgetProduct")
            self.listWidgetCategory = self.MainWindow.findChild(QListWidget, "listWidgetCategory")
            self.pushButtonSearchBill = self.MainWindow.findChild(QPushButton, "pushButtonSearchBill")
            self.tableWidgetProduct.cellClicked.connect(self.display_product_info)
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi liên kết UI: {str(e)}")
            raise

    def _setup_table_columns(self):
        self.tableWidgetProduct.setColumnCount(5)
        self.tableWidgetProduct.setHorizontalHeaderLabels(["Mã SP", "Tên SP", "Giá", "Số lượng", "Mã danh mục"])
        self.tableWidgetProduct.setColumnWidth(0, 100)
        self.tableWidgetProduct.setColumnWidth(1, 200)
        self.tableWidgetProduct.setColumnWidth(2, 150)
        self.tableWidgetProduct.setColumnWidth(3, 100)
        self.tableWidgetProduct.setColumnWidth(4, 150)

    def Signal(self):
        self.listWidgetCategory.itemClicked.connect(self.filter_products)
        self.pushButtonCloseInventory.clicked.connect(self.back_SalesWindow)
        self.pushButtonNew.clicked.connect(self.xuly_moi)
        self.pushButtonAddProduct.clicked.connect(self.xuly_them)
        self.pushButtonRemoveProduct.clicked.connect(self.xuly_xoa)
        self.pushButtonSearchBill.clicked.connect(self.open_bill_summary)

    def showWindow(self):
        self.MainWindow.show()

    def load_categories(self):
        self.listWidgetCategory.clear()
        for category in self.categories:
            cate_item = QListWidgetItem(f"{category.cateid} - {category.catename}")
            self.listWidgetCategory.addItem(cate_item)

    def load_products(self):
        self.tableWidgetProduct.setRowCount(0)
        self.total_quantity = 0
        for product in self.products:
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
            col_proid = QTableWidgetItem(product.proid)
            col_proname = QTableWidgetItem(product.proname)
            col_price = QTableWidgetItem(str(product.price))
            col_quantity = QTableWidgetItem(str(product.quantity))
            col_cateid = QTableWidgetItem(str(product.cateid))
            self.tableWidgetProduct.setItem(row, 0, col_proid)
            self.tableWidgetProduct.setItem(row, 1, col_proname)
            self.tableWidgetProduct.setItem(row, 2, col_price)
            self.tableWidgetProduct.setItem(row, 3, col_quantity)
            self.tableWidgetProduct.setItem(row, 4, col_cateid)
            self.total_quantity += product.quantity
            if product.quantity < 10:
                col_proid.setBackground(Qt.GlobalColor.red)
                col_proname.setBackground(Qt.GlobalColor.red)
                col_price.setBackground(Qt.GlobalColor.red)
                col_quantity.setBackground(Qt.GlobalColor.red)
                col_cateid.setBackground(Qt.GlobalColor.red)
    def show_products_gui(self):
        self.tableWidgetProduct.setRowCount(0)
        self.products = self.dc.get_all_products()
        self.load_products()

    def filter_products(self):
        row = self.listWidgetCategory.currentRow()
        if row < 0:
            return

        self.selected_cate = self.categories[row]
        current_cateid = self.selected_cate.cateid

        if self.is_filtered and self.last_filtered_cateid == current_cateid:
            self.show_products_gui()
            self.is_filtered = False
            self.last_filtered_cateid = None
        else:
            self.products = self.dc.get_product_bycategories(current_cateid)
            self.tableWidgetProduct.setRowCount(0)
            self.total_quantity = 0
            for product in self.products:
                row = self.tableWidgetProduct.rowCount()
                self.tableWidgetProduct.insertRow(row)
                self.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(product.proid))
                self.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(product.proname))
                self.tableWidgetProduct.setItem(row, 2, QTableWidgetItem(str(product.price)))
                self.tableWidgetProduct.setItem(row, 3, QTableWidgetItem(str(product.quantity)))
                self.tableWidgetProduct.setItem(row, 4, QTableWidgetItem(product.cateid))
                self.total_quantity += product.quantity
            self.is_filtered = True
            self.last_filtered_cateid = current_cateid

    def display_product_info(self, row, column):
        try:
            product_id = self.tableWidgetProduct.item(row, 0).text()
            product_name = self.tableWidgetProduct.item(row, 1).text()
            product_price = self.tableWidgetProduct.item(row, 2).text()
            product_quantity = self.tableWidgetProduct.item(row, 3).text()
            product_cate_id = self.tableWidgetProduct.item(row, 4).text()
            self.lineEditProID.setText(product_id)
            self.lineEditProName.setText(product_name)
            self.lineEditPrice.setText(product_price)
            self.lineEditQuantity.setText(product_quantity)
            self.lineEditCateID.setText(product_cate_id)
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể hiển thị thông tin sản phẩm: {str(e)}")

    def xuly_moi(self):
        self.lineEditProID.clear()
        self.lineEditProName.clear()
        self.lineEditPrice.clear()
        self.lineEditQuantity.clear()
        self.lineEditCateID.clear()

    def xuly_them(self):
        try:
            proid = self.lineEditProID.text().strip()
            proname = self.lineEditProName.text().strip()
            price = self.lineEditPrice.text().strip()
            quantity = self.lineEditQuantity.text().strip()
            cateid = self.lineEditCateID.text().strip()

            if not all([proid, proname, price, quantity, cateid]):
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
                return

            try:
                price = float(price)
                quantity = int(quantity)
            except ValueError:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Giá hoặc số lượng không hợp lệ!")
                return

            new_product = Product(proid=proid, proname=proname, price=price, quantity=quantity, cateid=cateid)
            products = self.dc.get_all_products()
            if any(p.proid == proid for p in products):
                QMessageBox.critical(self.MainWindow, "Lỗi", "Mã sản phẩm đã tồn tại!")
                return

            products.append(new_product)
            jff = JsonFileFactory()
            jff.write_data(products, "../dataset/products.json")
            self.products = products
            self.load_products()
            QMessageBox.information(self.MainWindow, "Thành công", "Đã thêm sản phẩm!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể thêm sản phẩm: {str(e)}")

    def xuly_xoa(self):
        try:
            selected_row = self.tableWidgetProduct.currentRow()
            if selected_row < 0:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn sản phẩm để xóa!")
                return

            proid = self.tableWidgetProduct.item(selected_row, 0).text()
            products = self.dc.get_all_products()
            products = [p for p in products if p.proid != proid]
            jff = JsonFileFactory()
            jff.write_data(products, "../dataset/products.json")
            self.products = products
            self.load_products()
            QMessageBox.information(self.MainWindow, "Thành công", "Đã xóa sản phẩm!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xóa sản phẩm: {str(e)}")

    def back_SalesWindow(self):
        from DoAnCuoiKy.ui.SalesMainWindowEx import SalesMainWindowEx
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = SalesMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def open_bill_summary(self):
        from DoAnCuoiKy.ui.BillSummaryEx import BillSummaryEx
        self.bill_summary_window = QMainWindow()
        self.bill_summary_ui = BillSummaryEx()
        self.bill_summary_ui.setupUi(self.bill_summary_window)
        self.bill_summary_window.show()
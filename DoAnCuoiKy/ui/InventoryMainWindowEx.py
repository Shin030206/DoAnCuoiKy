import sys

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QTableWidget, QTableWidgetItem, QListWidgetItem, \
    QListWidget

from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Product import Product
from DoAnCuoiKy.ui.InventoryMainWindow import Ui_MainWindow



class InventoryMainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.categories = None
        self.products = []
        self.total_quantity = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self._setup_table_columns()
        self._link_ui_components()
        self.Signal()
        self.load_products()
        self.load_categories()  # Tải danh sách danh mục

    def _link_ui_components(self):
        try:
            # Liên kết các QLineEdit và QTableWidget sản phẩm
            self.lineEditProID = self.MainWindow.findChild(QLineEdit, "lineEditProID")
            self.lineEditProName = self.MainWindow.findChild(QLineEdit, "lineEditProName")
            self.lineEditPrice = self.MainWindow.findChild(QLineEdit, "lineEditPrice")
            self.lineEditQuantity = self.MainWindow.findChild(QLineEdit, "lineEditQuantity")
            self.lineEditCateID = self.MainWindow.findChild(QLineEdit, "lineEditCateID")
            self.tableWidgetProduct = self.MainWindow.findChild(QTableWidget, "tableWidgetProduct")

            # Liên kết QListWidget danh mục
            self.listWidgetCategory = self.MainWindow.findChild(QListWidget, "listWidgetCategory")

            # Kết nối sự kiện khi người dùng chọn một hàng trong bảng sản phẩm
            self.tableWidgetProduct.cellClicked.connect(self.display_product_info)

            # Kết nối sự kiện khi người dùng chọn một danh mục
            self.listWidgetCategory.itemSelectionChanged.connect(self.filter_products)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi liên kết UI: {str(e)}")
            raise
    def display_product_info(self, row, column):
        """Hiển thị thông tin sản phẩm lên các QLineEdit khi người dùng chọn một hàng trong bảng"""
        try:
            # Lấy thông tin từ hàng được chọn
            product_id = self.tableWidgetProduct.item(row, 0).text()
            product_name = self.tableWidgetProduct.item(row, 1).text()
            product_price = self.tableWidgetProduct.item(row, 2).text()
            product_quantity = self.tableWidgetProduct.item(row, 3).text()
            product_cate_id = self.tableWidgetProduct.item(row, 4).text()

            # Hiển thị thông tin lên các QLineEdit
            self.lineEditProID.setText(product_id)
            self.lineEditProName.setText(product_name)
            self.lineEditPrice.setText(product_price)
            self.lineEditQuantity.setText(product_quantity)
            self.lineEditCateID.setText(product_cate_id)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể hiển thị thông tin sản phẩm: {str(e)}")

    def load_categories(self):
        """Tải danh sách danh mục và hiển thị lên QListWidget"""
        try:
            connector = DataConnector()
            self.categories = connector.get_all_categories()

            # Xóa danh sách cũ trong QListWidget
            self.listWidgetCategory.clear()

            # Thêm danh sách danh mục vào QListWidget
            for category in self.categories:
                cate_item = QListWidgetItem(f"{category.cateid} - {category.catename}")
                self.listWidgetCategory.addItem(cate_item)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tải danh sách danh mục: {str(e)}")
    def display_product_info(self, row, column):
        """Hiển thị thông tin sản phẩm lên các QLineEdit khi người dùng chọn một hàng trong bảng"""
        try:
            # Lấy thông tin từ hàng được chọn
            product_id = self.tableWidgetProduct.item(row, 0).text()
            product_name = self.tableWidgetProduct.item(row, 1).text()
            product_price = self.tableWidgetProduct.item(row, 2).text()
            product_quantity = self.tableWidgetProduct.item(row, 3).text()
            product_cate_id = self.tableWidgetProduct.item(row, 4).text()

            # Hiển thị thông tin lên các QLineEdit
            self.lineEditProID.setText(product_id)
            self.lineEditProName.setText(product_name)
            self.lineEditPrice.setText(product_price)
            self.lineEditQuantity.setText(product_quantity)
            self.lineEditCateID.setText(product_cate_id)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể hiển thị thông tin sản phẩm: {str(e)}")
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
        self.lineEditCateID.clear()

    def xuly_them(self):
        try:
            # Lấy dữ liệu từ các ô nhập
            product_id = self.lineEditProID.text().strip()
            product_name = self.lineEditProName.text().strip()
            product_price = self.lineEditPrice.text().strip()
            product_quantity = self.lineEditQuantity.text().strip()
            product_cate_id = self.lineEditCateID.text().strip()  # Lấy cateid từ QLineEdit

            # Kiểm tra dữ liệu trống
            if not all([product_id, product_name, product_price, product_quantity, product_cate_id]):
                QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng điền đầy đủ thông tin!")
                return

            # Kiểm tra định dạng số
            try:
                product_price = float(product_price)
                product_quantity = int(product_quantity)
            except ValueError:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Giá/số lượng không hợp lệ!")
                return

            # Thêm dữ liệu vào bảng và file JSON (giữ nguyên phần này)
            ...

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Không thể thêm sản phẩm: {str(e)}")

    def xuly_xoa(self):
        try:
            selected_row = self.tableWidgetProduct.currentRow()
            if selected_row >= 0:
                # Lấy mã sản phẩm từ hàng được chọn
                product_id = self.tableWidgetProduct.item(selected_row, 0).text()

                # Xóa khỏi JSON
                connector = DataConnector()
                products = connector.get_all_products()
                products = [p for p in products if p.proid != product_id]

                jff = JsonFileFactory()
                jff.write_data(products, "../dataset/products.json")

                # Xóa khỏi bảng và cập nhật tổng số lượng
                quantity = int(self.tableWidgetProduct.item(selected_row, 3).text())
                self.total_quantity -= quantity
                self.tableWidgetProduct.removeRow(selected_row)
            else:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn sản phẩm cần xóa!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể xóa: {str(e)}")

    def _setup_table_columns(self):
        """Cấu hình số cột và tiêu đề cho bảng"""
        self.tableWidgetProduct.setColumnCount(5)
        self.tableWidgetProduct.setHorizontalHeaderLabels([
            "Mã SP", "Tên SP", "Giá", "Số lượng", "Mã danh mục"
        ])
        # Đặt độ rộng cột (tuỳ chỉnh)
        self.tableWidgetProduct.setColumnWidth(0, 100)
        self.tableWidgetProduct.setColumnWidth(1, 200)
        self.tableWidgetProduct.setColumnWidth(2, 150)
        self.tableWidgetProduct.setColumnWidth(3, 100)
        self.tableWidgetProduct.setColumnWidth(4, 150)

    def load_products(self):
        try:
            connector = DataConnector()
            products = connector.get_all_products()
            self.tableWidgetProduct.setRowCount(0)  # Xóa toàn bộ hàng cũ trước khi tải mới

            for product in products:
                row = self.tableWidgetProduct.rowCount()
                self.tableWidgetProduct.insertRow(row)

                # Kiểm tra dữ liệu trước khi thêm vào bảng
                if product.proid and product.proname and product.price and product.quantity and product.cateid:
                    self.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(str(product.proid)))
                    self.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(product.proname))
                    self.tableWidgetProduct.setItem(row, 2, QTableWidgetItem(f"{product.price:,.2f}"))
                    self.tableWidgetProduct.setItem(row, 3, QTableWidgetItem(str(product.quantity)))
                    self.tableWidgetProduct.setItem(row, 4, QTableWidgetItem(product.cateid))
                else:
                    print(f"Sản phẩm {product.proid} thiếu thông tin, bỏ qua!")

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không tải được sản phẩm: {str(e)}")

    def filter_products(self):
        """Lọc sản phẩm theo danh mục được chọn"""
        try:
            # Lấy danh mục được chọn
            selected_row = self.listWidgetCategory.currentRow()
            if selected_row < 0:  # Không có danh mục nào được chọn
                return

            selected_category = self.categories[selected_row]

            # Lọc sản phẩm theo danh mục
            connector = DataConnector()
            self.products = connector.get_product_bycategories(selected_category.cateid)

            # Hiển thị sản phẩm lên QTableWidget
            self.show_products_gui()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể lọc sản phẩm: {str(e)}")

    def show_products_gui(self):
        """Hiển thị danh sách sản phẩm lên QTableWidget"""
        try:
            # Xóa toàn bộ hàng cũ trong QTableWidget
            self.tableWidgetProduct.setRowCount(0)

            # Thêm danh sách sản phẩm vào QTableWidget
            for product in self.products:
                row = self.tableWidgetProduct.rowCount()
                self.tableWidgetProduct.insertRow(row)

                # Tạo các cột cho hàng
                col_proid = QTableWidgetItem(product.proid)
                col_proname = QTableWidgetItem(product.proname)
                col_price = QTableWidgetItem(f"{product.price:,.2f}")
                col_quantity = QTableWidgetItem(str(product.quantity))
                col_cateid = QTableWidgetItem(product.cateid)

                # Đặt giá trị cho các cột
                self.tableWidgetProduct.setItem(row, 0, col_proid)
                self.tableWidgetProduct.setItem(row, 1, col_proname)
                self.tableWidgetProduct.setItem(row, 2, col_price)
                self.tableWidgetProduct.setItem(row, 3, col_quantity)
                self.tableWidgetProduct.setItem(row, 4, col_cateid)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể hiển thị sản phẩm: {str(e)}")
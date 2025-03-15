
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QListWidgetItem, QMessageBox, QSpinBox

from DoAnCuoiKy.libs.DataConnector import DataConnector
from DoAnCuoiKy.ui.SalesMainWindow import Ui_MainWindow


class SalesMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dc=DataConnector()
        self.categories=self.dc.get_all_categories()
        self.products=self.dc.get_all_products()
        self.selected_cate = None
        self.selected_product = None
        # Tạo QSpinBox để nhập số lượng
        self.spinBoxQuantity = QSpinBox()
        self.spinBoxQuantity.setMinimum(1)  # Giá trị tối thiểu là 1
        self.spinBoxQuantity.setMaximum(100)  # Giá trị tối đa là 100 (tuỳ chỉnh)
        self.spinBoxQuantity.setValue(1)  # Giá trị mặc định

        # Thêm QSpinBox vào layout (ví dụ: QHBoxLayout hoặc QVBoxLayout)
        self.verticalLayout_2.addWidget(self.spinBoxQuantity)  # Thay "self.layout" bằng layout thực tế của bạn
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.Signal()
        self.show_catagories_gui()
        self.show_products_gui()
    def showWindow(self):
        self.MainWindow.show()
    def Signal(self):
        self.listWidgetCategory.itemSelectionChanged.connect(self.filter_products)
        self.pushButtonInventory.clicked.connect(self.process_Inventory)
        self.pushButtonAddBill.clicked.connect(self.add_to_bill)
        self.pushButtonRemoveFromBill.clicked.connect(self.remove_from_bill)
        self.pushButtonNewSales.clicked.connect(self.new_Sales)
        self.pushButtonCalculate.clicked.connect(self.update_total_display)
    def process_Inventory(self):
        from DoAnCuoiKy.ui.InventoryMainWindowEx import InventoryMainWindowEx
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = InventoryMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def new_Sales(self):
        # Kiểm tra xem có sản phẩm trong hóa đơn không
        if not hasattr(self, 'item_quantities') or not self.item_quantities:
            return  # Không có gì để xử lý

        # Trả lại số lượng cho từng sản phẩm trong kho
        for proid, quantity in self.item_quantities.items():
            product = self.dc.get_product_by_proid(proid)
            if product:
                self.dc.update_add_quantity(product, quantity)

        # Xóa toàn bộ hóa đơn
        self.listWidgetBill.clear()
        self.item_quantities = {}  # Reset dictionary

        # Cập nhật giao diện
        self.show_products_gui()
    def show_catagories_gui(self):
        # clear Layout
        self.listWidgetCategory.clear()
        for cate in self.categories:
            item = QListWidgetItem(str(cate))
            self.listWidgetCategory.addItem(item)

    def show_products_gui(self):
        # clear Layout
        self.tableWidgetProduct.setRowCount(0)
        self.products=self.dc.get_all_products()
        # load products
        for product in self.products:
            # get number of row(meaning last index)
            row = self.tableWidgetProduct.rowCount()
            # insert new row(last row, at the end of row in the table)
            self.tableWidgetProduct.insertRow(row)
            col_proid = QTableWidgetItem(product.proid)
            col_proname = QTableWidgetItem(product.proname)
            col_price = QTableWidgetItem(str(product.price))
            col_quantity = QTableWidgetItem(str(product.quantity))
            col_cateid = QTableWidgetItem(str(product.cateid))
            # set column for row:
            self.tableWidgetProduct.setItem(row, 0, col_proid)
            self.tableWidgetProduct.setItem(row, 1, col_proname)
            self.tableWidgetProduct.setItem(row, 2, col_price)
            self.tableWidgetProduct.setItem(row, 3, col_quantity)
            self.tableWidgetProduct.setItem(row, 4, col_cateid)
    def filter_products(self):
        #get current selected index
        row=self.listWidgetCategory.currentRow()
        if row<0:#not found selected index
            return
        self.selected_cate=self.categories[row]
        #filter products by cate id
        self.products=self.dc.get_product_bycategories(self.selected_cate.cateid)
        #re-display products into QTableWidget
        self.tableWidgetProduct.setRowCount(0)
        for product in self.products:
            # get number of row(meaning last index)
            row = self.tableWidgetProduct.rowCount()
            # insert new row(last row, at the end of row in the table)
            self.tableWidgetProduct.insertRow(row)
            col_proid = QTableWidgetItem(product.proid)
            col_proname = QTableWidgetItem(product.proname)
            col_price = QTableWidgetItem(str(product.price))
            col_quantity = QTableWidgetItem(str(product.quantity))
            col_cateid = QTableWidgetItem(str(product.cateid))
            # set column for row:
            self.tableWidgetProduct.setItem(row, 0, col_proid)
            self.tableWidgetProduct.setItem(row, 1, col_proname)
            self.tableWidgetProduct.setItem(row, 2, col_price)
            self.tableWidgetProduct.setItem(row, 3, col_quantity)
            self.tableWidgetProduct.setItem(row, 4, col_cateid)

    def add_to_bill(self):
        try:
            # 1. Kiểm tra người dùng đã chọn sản phẩm chưa
            selected_items = self.tableWidgetProduct.selectedItems()
            if not selected_items:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Vui lòng chọn sản phẩm từ danh sách!")
                return

            # 2. Lấy thông tin sản phẩm từ item được chọn
            selected_item = selected_items[0]

            # Giả sử định dạng item: "P001 | Áo thun | 100,000 VND | 10"
            item_data = selected_item.text().split(" | ")
            if len(item_data) < 4:
                QMessageBox.critical(self.MainWindow, "Lỗi", "Định dạng sản phẩm không hợp lệ!")
                return

            proid = item_data[0].strip()  # Lấy mã sản phẩm

            # 3. Lấy số lượng từ SpinBox
            quantity = self.spinBoxQuantity.value()
            if quantity <= 0:
                QMessageBox.warning(self.MainWindow, "Cảnh báo", "Số lượng phải lớn hơn 0!")
                return

            # 4. Lấy thông tin sản phẩm từ database
            product = self.dc.get_product_by_proid(proid)
            if not product:
                QMessageBox.critical(self.MainWindow, "Lỗi", f"Sản phẩm {proid} không tồn tại trong hệ thống!")
                return

            # 5. Kiểm tra số lượng tồn kho
            if product.quantity < quantity:
                QMessageBox.warning(
                    self.MainWindow,
                    "Cảnh báo",
                    f"Số lượng tồn kho không đủ!\nHiện có: {product.quantity} sản phẩm"
                )
                return

            # 6. Cập nhật số lượng tồn kho (GIẢM)
            new_quantity = product.quantity - quantity
            self.dc.update_remove_quantity(new_quantity)

            # 7. Thêm vào hóa đơn
            if proid in self.item_quantities:
                self.item_quantities[proid] += quantity
            else:
                self.item_quantities[proid] = quantity

            # 8. Thêm vào ListWidget Bill
            bill_item = (
                f"{product.proid} | {product.name} | "
                f"SL: {quantity} | "
                f"{product.price:,.0f} VND x {quantity} = "
                f"{(product.price * quantity):,.0f} VND"
            )
            self.listWidgetBill.addItem(bill_item)

            # 9. Cập nhật giao diện
            self.show_products_gui()  # Load lại danh sách sản phẩm với số lượng mới
            self.update_total_display()  # Cập nhật tổng tiền

        except Exception as e:
            QMessageBox.critical(
                self.MainWindow,
                "Lỗi nghiêm trọng",
                f"Lỗi khi thêm vào hóa đơn: {str(e)}"
            )
    def remove_from_bill(self):
        # Lấy item được chọn từ list bill
        current_item = self.listWidgetBill.currentItem()
        if not current_item:
            return

        # Trích xuất thông tin từ item
        item_data = current_item.text().split('\t')
        cur_proid = item_data[0]
        cur_proname = item_data[1]
        cur_price = item_data[2]
        current_quantity = int(item_data[3])  # Số lượng hiện tại trong bill
        cur_cateid = item_data[4]

        # Kiểm tra và khởi tạo dictionary nếu chưa có
        if not hasattr(self, 'item_quantities'):
            self.item_quantities = {}

        # Giảm số lượng trong bill
        if cur_proid in self.item_quantities:
            # Giảm số lượng và kiểm tra
            self.item_quantities[cur_proid] -= 1

            # Nếu số lượng <= 0 thì xóa khỏi bill
            if self.item_quantities[cur_proid] <= 0:
                # Xóa item khỏi list widget
                row = self.listWidgetBill.row(current_item)
                self.listWidgetBill.takeItem(row)

                # Xóa khỏi dictionary
                del self.item_quantities[cur_proid]
            else:
                # Cập nhật số lượng mới
                current_item.setText(
                    f'{cur_proid}\t{cur_proname}\t{cur_price}\t{self.item_quantities[cur_proid]}\t{cur_cateid}'
                )
        else:
            # Trường hợp không tồn tại trong dictionary (không nên xảy ra)
            return

        # Tăng số lượng trong kho và cập nhật giao diện
        selected_product = next((p for p in self.products if p.proid == cur_proid), None)
        if selected_product:
            self.dc.update_add_quantity(selected_product)  # Hàm tăng quantity trong database
            self.show_products_gui()  # Refresh danh sách sản phẩm

    def calculate_total(self):
        try:
            total = 0
            for proid, quantity in self.item_quantities.items():
                product = self.dc.get_product_by_proid(proid)
                if product and quantity > 0:
                    total += product.price * quantity  # Tính tổng trước thuế
            total *= 1.08  # Áp dụng thuế 8% một lần duy nhất
            return total
        except Exception as e:
            print(f"Lỗi tính tổng tiền: {str(e)}")
            return 0

    def update_total_display(self):
        try:
            if not self.item_quantities:
                QMessageBox.information(self.MainWindow, "Thông báo", "Hóa đơn trống!")
                return

            message = "=== HÓA ĐƠN BÁN HÀNG ===\n"
            total_before_tax = 0  # Tổng trước thuế
            tax_rate = 0.08  # Thuế 8%

            # Duyệt qua từng sản phẩm để xây dựng thông tin chi tiết
            for proid, quantity in self.item_quantities.items():
                product = self.dc.get_product_by_proid(proid)
                if not product:
                    # Thông báo lỗi và dừng hàm
                    QMessageBox.critical(
                        self.MainWindow,
                        "Lỗi",
                        f"Sản phẩm với mã '{proid}' không tồn tại trong hệ thống!"
                    )
                    return  # Dừng ngay nếu có lỗi

                item_total = product.price * quantity
                total_before_tax += item_total

                # Thêm thông tin sản phẩm vào message
                message += (
                    f"{product.name}\n"
                    f" - Mã SP: {product.proid}\n"
                    f" - Số lượng: {quantity}\n"
                    f" - Đơn giá: {product.price:,.0f} VND\n"
                    f" - Thành tiền: {item_total:,.0f} VND\n\n"
                )

            # Tính tổng sau thuế
            total_with_tax = total_before_tax * (1 + tax_rate)

            # Thêm tổng tiền vào message
            message += (
                "--------------------------------\n"
                f"Tổng tiền (trước thuế): {total_before_tax:,.0f} VND\n"
                f"Thuế VAT ({tax_rate * 100}%): {total_before_tax * tax_rate:,.0f} VND\n"
                f"TỔNG CỘNG: {total_with_tax:,.0f} VND"
            )

            # Hiển thị hóa đơn
            QMessageBox.information(self.MainWindow, "Hóa đơn", message)

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Không thể tính tiền: {str(e)}")
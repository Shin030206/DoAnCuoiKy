
import json
from datetime import datetime

from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Category import Category
from DoAnCuoiKy.models.Employee import Employee
from DoAnCuoiKy.models.Product import Product


class DataConnector:
    def get_all_employee(self):
        jff = JsonFileFactory()
        filename = "../dataset/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def get_all_categories(self):
        categories = []
        jff = JsonFileFactory()
        filename = '../dataset/categories.json'
        categories = jff.read_data(filename, Category)
        return categories
    def get_all_products(self):
        products = []
        jff = JsonFileFactory()
        filename = '../dataset/products.json'
        products = jff.read_data(filename, Product)
        return products
    def get_product_bycategories(self,cateid):
        products=self.get_all_products()
        result=[]
        for product in products:
            if product.cateid==cateid:
                result.append(product)
        return result
    def login(self,username,password):
        employees=self.get_all_employee()
        for e in employees:
            if e.UserName==username and e.PassWord==password:
                return e
        return None

    def save_bill(self, total_amount, items):
        """Lưu hóa đơn vào file JSON"""
        try:
            # Đọc danh sách bill hiện tại
            with open("../dataset/bills.json", "r") as f:
                bills = json.load(f)
        except FileNotFoundError:
            bills = []

        # Tạo bill mới
        new_bill = {
            "bill_id": f"B{datetime.now().strftime('%Y%m%d%H%M%S')}",  # Tạo ID duy nhất
            "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_amount": total_amount,
            "status": "Paid",
            "items": items  # Danh sách sản phẩm trong hóa đơn
        }

        # Thêm vào danh sách và lưu lại
        bills.append(new_bill)
        with open("../dataset/bills.json", "w") as f:
            json.dump(bills, f, indent=4)

    def get_all_bills(self):
        """Lấy tất cả hóa đơn từ file JSON"""
        try:
            with open("../dataset/bills.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    def get_bills_by_date_range(self, from_date, to_date):
        # Giả sử bạn lấy dữ liệu từ cơ sở dữ liệu
        bills = self._fetch_bills_from_database()
        if bills is None:
            return []
        # Lọc các hóa đơn trong khoảng thời gian
        filtered_bills = [bill for bill in bills if from_date <= bill.date_created <= to_date]
        return filtered_bills

    def get_bill_details(self, bill_id):
        # Giả sử bạn lấy dữ liệu từ cơ sở dữ liệu
        bills = self._fetch_bills_from_database()
        if bills is None:
            return None
        # Tìm hóa đơn có bill_id tương ứng
        for bill in bills:
            if bill.bill_id == bill_id:
                return bill
        return None  # Trả về None nếu không tìm thấy

import json
import os
from datetime import datetime

from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Category import Category
from DoAnCuoiKy.models.Manager import Manager
from DoAnCuoiKy.models.Product import Product
from DoAnCuoiKy.models.Staff import Staff

class SalesRecord:
    def __init__(self, datetime, items, total):
        self.datetime = datetime
        self.items = items  # items là list các dict
        self.total = total

    # Thêm phương thức để hỗ trợ khởi tạo từ dict
    @classmethod
    def from_dict(cls, data):
        return cls(
            datetime=data.get("datetime"),
            items=data.get("items"),
            total=data.get("total")
        )
class DataConnector:
    def get_all_bills(self):
        jff = JsonFileFactory()
        filename = "../dataset/sales_history.json"
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [{"bill_id": f"B{idx+1:04d}", "date_created": item["datetime"], "total_amount": item["total"], "status": "Hoàn thành", "items": item["items"]} for idx, item in enumerate(data)]
        return []

    def get_bills_by_date_range(self, from_date, to_date):
        bills = self.get_all_bills()
        from_dt = datetime.strptime(from_date, "%Y-%m-%d")
        to_dt = datetime.strptime(to_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
        filtered_bills = []
        for bill in bills:
            bill_dt = datetime.strptime(bill["date_created"], "%Y-%m-%d %H:%M:%S")
            if from_dt <= bill_dt <= to_dt:
                filtered_bills.append(bill)
        return filtered_bills

    def get_bill_details(self, bill_id):
        bills = self.get_all_bills()
        for bill in bills:
            if bill["bill_id"] == bill_id:
                return [{"product_name": item["proname"], "quantity": item["quantity"], "price": item["price"]} for item in bill["items"]]
        return []
    def get_all_staff(self):
        jff = JsonFileFactory()
        filename = "../dataset/staff.json"
        staffs = jff.read_data(filename, Staff)
        return staffs
    def get_all_manager(self):
        jff = JsonFileFactory()
        filename = "../dataset/manager.json"
        managers = jff.read_data(filename, Manager)
        return managers
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
    def find_index_product(self,proid):
        self.products=self.get_all_products()
        for i in range(len(self.products)):
            product=self.products[i]
            if product.proid==proid:
                return i
        return -1

    def get_product_by_proid(self, proid):
        self.products=self.get_all_products()# Tìm sản phẩm trong danh sách dựa trên proid
        for product in self.products:  # Giả định self.products là danh sách sản phẩm
            if product.proid == proid:
                return product
        return None

    # Trong DataConnector.py
    def update_product_quantity(self, proid, new_quantity):
        self.products=self.get_all_products()
        for product in self.products:
            if product.proid == proid:
                product.quantity = new_quantity
                self.save_update_product(product)
                return
        raise ValueError(f"Sản phẩm {proid} không tồn tại!")
    def save_update_product(self,current_product):
        index=self.find_index_product(current_product.proid)
        if index!=-1:
            self.products[index]=current_product
            jff = JsonFileFactory()
            filename = '../dataset/products.json'
            jff.write_data(self.products, filename)
    def update_remove_quantity(self,current_product):
        index = self.find_index_product(current_product.proid)
        if index != -1:
            self.products[index] = current_product
            current_product.quantity=current_product.quantity-1
            self.save_update_product(current_product)
    def update_add_quantity(self,current_product,quantity=1):
        index = self.find_index_product(current_product.proid)
        if index != -1:
            self.products[index] = current_product
            current_product.quantity+=quantity
            self.save_update_product(current_product)
    def login(self, user_role, username, password):
        if user_role == 'st':
            st = self.get_all_staff()
            for s in st:
                if s.UserName == username and s.PassWord == password:
                    return "st"
            return None
        elif user_role == 'mg':
            mg = self.get_all_manager()
            for m in mg:
                if m.UserName == username and m.PassWord == password:
                    return "mg"
            return None

    def save_sales_history(self, bill_data):
        jff = JsonFileFactory()
        filename = "../dataset/sales_history.json"

        try:
            # Đọc dữ liệu thô từ file thủ công
            if os.path.isfile(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    existing_data = json.load(file)  # Đọc trực tiếp bằng json.load
            else:
                existing_data = []
            if existing_data is None or not isinstance(existing_data, list):
                existing_data = []  # Gán danh sách rỗng nếu không có dữ liệu
            sales_records = []
            for item in existing_data:
                if isinstance(item, dict):
                    # Chỉ lấy các khóa hợp lệ cho SalesRecord
                    sales_record = SalesRecord(
                        datetime=item.get("datetime"),
                        items=item.get("items"),
                        total=item.get("total")
                    )
                    sales_records.append(sales_record)

            # Tạo SalesRecord từ bill_data
            new_sales_record = SalesRecord(
                datetime=bill_data.get("datetime"),
                items=bill_data.get("items"),
                total=bill_data.get("total")
            )
            sales_records.append(new_sales_record)

            # Ghi lại dữ liệu
            jff.write_data(sales_records, filename)
        except Exception as e:
            print(f"Lỗi khi lưu lịch sử: {str(e)}")
            raise  # Để xem chi tiết lỗi nếu cần

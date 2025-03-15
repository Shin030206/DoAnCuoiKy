from DoAnCuoiKy.libs.JsonFileFactory import JsonFileFactory
from DoAnCuoiKy.models.Category import Category
from DoAnCuoiKy.models.Manager import Manager
from DoAnCuoiKy.models.Product import Product
from DoAnCuoiKy.models.Staff import Staff


class DataConnector:
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
        # Loại bỏ khoảng trắng thừa và chuyển về chữ thường (nếu cần)
        cleaned_proid = proid.strip().lower()
        for product in self.products:
            if product.proid.strip().lower() == cleaned_proid:
                return product
        return None
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
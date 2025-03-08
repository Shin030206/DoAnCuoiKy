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

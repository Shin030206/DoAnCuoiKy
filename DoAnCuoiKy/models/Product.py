class Product:
    def __init__(self,proid,proname,price,quantity,cateid=None):
        self.proid=proid
        self.proname=proname
        self.price=price
        self.quantity=quantity
        self.cateid=cateid
    def __str__(self):
        return f'{self.proid}\t{self.proname}\t{self.price}\t{self.cateid}'
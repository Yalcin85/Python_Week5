class Product:
    def __init__(self):
        self.id = None
        self.name = None
        self.purchase_price = None
        self.sale_price = None
        self.remarks = None

    def set_remarks(self):
        if self.sale_price - self.purchase_price < 0:
            self.remarks = "Loss"
        else:
            self.remarks = "Profit"

    def set_details(self):
        self.id = input("İd : ")
        self.name = input("Name : ")
        self.purchase_price = float(input("Purchase price : "))
        self.sale_price = float(input("Sale price : "))
        self.set_remarks()

    def get_details(self):
        print(f"{self.name} of {self.id} is purchase price {self.purchase_price}, sale price {self.sale_price}\nRemarks : {self.remarks}")

per = Product()
per.set_details()
per.get_details()

class ItemInfo:
    def __init__(self):
        self.item_code = 0
        self.item = None
        self.price = None
        self.qty = None
        self.discount = None
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty < 20:
            self.discount = 15
        else:
            self.discount = 20
        self.net_price = (self.price * self.qty) - self.discount
    def buy(self):
        self.item_code = input("İtem Code : ")
        self.item = input("İtem : ")
        self.price = float(input("Price : "))
        self.qty = int(input("Quantity in stock : "))
    def show_all(self):
        return f"{self.item} with {self.item_code} is price {self.price}.\nQuantity in stock is {self.qty} and discount is {self.discount}.\nPrice after discount is {self.net_price}"

per=ItemInfo()
per.buy()
per.calculate_discount()
print(per.show_all())
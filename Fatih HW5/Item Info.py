'''
Define a class named ``ItemInfo` with the following description:

item_code(Item Code), item(item name), price(Price of each item), 
qty(quantity in stock), discount(Discount percentage on the item), 
net_price(Price after discount)

Methods :

A member method calculate_discount() to calculate discount as per 
the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and 
price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, 
price, qty. Then call function calculate_discount() to calculate the discount 
and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all

 the data members.

'''
class ItemInfo():
    def __init__(self) :
        self.item_code = 0
        self.net_price= None
        self.qty = None
        self.price = None
        self.discount = None
    def buy(self):
        self.item_code = input("Please enter  an item code :")
        self.itemName = input("Please enter an item name: ")
        self.price = int(input("Please enter a price of item :"))
        self.qty = int(input("Please enter a quantity of item :"))
    def calculate_discount(self):
        if self.qty <= 10 : 
            self.discount = 0
        elif self.qty >= 11 and self.qty < 20:
            self.discount = 15
        else :
            self.discount = 20
        self.net_price = self.price * self.qty - self.discount  
    def show_all(self):
        return f"{self.itemName} 's item code is: {self.item_code} and it's price is: {self.price}.\nQuantity is {self.qty}, discount of items {self.discount}.\n Net price is {self.net_price}"
info = ItemInfo()
info.buy()
info.calculate_discount()
print(info.show_all())

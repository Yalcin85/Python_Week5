
"""Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members."""

class iteminfo():
     
    def __init__(self,item_name):
        self.item_code = 0
        self.item_name = item_name
        self.price = int()
        self.net_price = int()
        self.qty = int()
        self.discount = int()
        
    
    def show_all(self):
        return print("item_name :", self.item_name,"||""item_code :", self.item_code,"||", \
                    "price: ", self.price,"||", "quantity : ",self.qty, \
                    "||","Discount : ",self.discount,"Net_price: ", self.net_price )

    @staticmethod
    def calculate_discount(qty):
        if qty <=10:
            discount = 0
        
        elif qty >=11 and qty<20:
            discount = 0.15
        
        elif qty >= 20:
            discount = 0.20
        return discount

    def buy(self, item_code, item_name, price, qty):
        self.discount=iteminfo.calculate_discount(qty)
        self.price=price
        self.net_price=float(self.price)- (self.price*self.discount)
        self.item_code=item_code
        self.item=item_name
        self.qty=qty

   
a=iteminfo("kalem")

a.show_all()

a.buy(11105,"kalem",150,20)

a.show_all()

        
        
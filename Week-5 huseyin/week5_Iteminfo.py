""" Define a class named ``ItemInfo` with the following description:

item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

Methods :

A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members."""


class ItemInfo:
    
    def __init__(self):
        self.discount=0
        self.net_price=0
        self.item_code=""
        self.item=""
        self.price=0
        self.qty=0
        
    def buy(self):
        self.item_code  =input("Please enter item code    : ")
        self.item       =input("Please enter item         : ")
        self.price      =float(input("Please enter price  : "))
        self.qty        =int(input("Please enter qty code : "))
    
    def calculate_discount(self):
        
        if self.qty <= 10 :
            self.discount=0   
        
        elif self.qty < 10 and self.qty <= 20 :
            self.discount=(self.price*self.qty*15)/100   
            
        elif self.qty >= 20 :
            self.discount=(self.price*self.qty*20)/100    
                
        self.net_price= self.price*self.qty - self.discount
         
    @property    
    def show_all(self):
        self.calculate_discount()
        print("Your discount: " , self.discount, "and" ,"Your net price :", self.net_price)
        
iteminfo_1=ItemInfo()
iteminfo_1.buy()
iteminfo_1.show_all

    
        
            
    
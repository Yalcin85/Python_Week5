"""Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
calculate_discount():
total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
shopping_cart():
Let user add items in the shopping basket. Be creative with the items, set their prices as well."""


class Customer:
    def __init__(self,username,phone_number):
        self.username           =username
        self.phone_number       =phone_number
        self.city               =str()
    
    def __str__(self):
        print(f"your username: {self.username}, your phone number: {self.phone_number}, your city:{self.city}" )
    
    def getCustomerNo(self):
        return self.username
       
class Items(Customer):
    def __init__(self,username,phone_number):
        super().__init__(username,phone_number)
        self.price=int()
        self.qty=int()
        self.total_price=int()
        
    def __str__(self):
        pass
    
    def shopping_cart(self):
        print("****************************************")
        print("\n""\t"
        "1 for iphone           :", 600,"\n""\t"\
        "2 for mac pro          :", 900,"\n""\t"\
        "3 for bike             :", 80,"\n""\t"\
        "4 for watch            :", 100,"\n""\t"\
        "5 for monitor          :", 300,"\n""\t"\
        "6 for backpack         :", 120)
        print("*****************************************")
        
        self.choise = (input("Please choise your items   :"))
        self.qty    = int(input("Please choise your quantity:"))
              
        if self.choise=="1":
            self.price=600
            self.total_price = self.price * self.qty
            return self.total_price
        
        elif self.choise=="2":
            self.price=900
            self.total_price = self.price * self.qty 
            return  self.total_price
        
        elif self.choise=="3":
            self.price=80
            self.total_price = self.price * self.qty
            return  self.total_price
        
        elif self.choise=="4":
            self.price=100
            self.total_price = self.price * self.qty 
            return  self.total_price
        
        elif self.choise=="5":
            self.price=300
            self.total_price = self.price * self.qty
            return  self.total_price
        
        elif self.choise=="6":
            self.price=120
            self.total_price = self.price * self.qty
            return  self.total_price  
            
    def calculate_discount(self):
           
        if self.total_price >= 4000:
            self.discount = self.total_price*0.25
            return self.discount
        
        elif self.total_price >= 2000:
            self.discount = self.total_price*0.15
            return self.discount
        
        elif self.total_price < 2000:
            self.discount = self.total_price*0.10
            return self.discount
            
                  
    def str(self):
        self.price_tobe_paid = self.total_price - self.discount
        print("Your username            :" , self.username,"\n"\
            "Your phone number          :" , self.phone_number,"\n"\
            "Your city                  :" , self.city,"\n"\
            "Your Total Price           :" , self.total_price,"\n"\
            "Your Discount              :" , self.discount,"\n"\
            "Your Tobe Paid             :",self.price_tobe_paid)

       
customers=Customer("hakan",123)
customers.__str__()
items=Items("hakan",123)
items.shopping_cart()
items.calculate_discount()
items.str()

   
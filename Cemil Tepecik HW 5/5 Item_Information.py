#============================STORE MANAGEMENT, ITEM INFORMATION================================
# Developer: Cemil Tepecik
# Date:02.03.2021
#Define a class named ``ItemInfo` with the following description:
#item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item),
# net_price(Price after discount)
#Methods :
#•	A member method calculate_discount() to calculate discount as per the following rules:
#•	If qty <= 10 —> discount is 0
#•	If qty (11 to 20 inclusive) —> discount is 15
#•	If qty >= 20 —> discount is 20
#•	A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
#•	A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
#•	A function show_all() or similar name to allow user to view the content of all the data members.
#------------------------class definition-------------------------------------------------
class ItemInfo:
    discount = 1  # no discount default case 11 to 20 inclusive —> discount is 15
    number_of_item=0
    def __init__(self,item_code,item_name,price,quantity):#discount,net_price):

        #net_price = 10
        self.item_code=item_code
        self.item_name=item_name
        self.price=price #initial price no change by amount
        self.qty=quantity
        self.discount=ItemInfo.discount
        ItemInfo.number_of_item += 1
    def discount_amount(self):
        if self.qty>=20:
            self.discount=0.8
        elif 10<self.qty<20:
            self.discount=0.85
        else:
            self.discount=1
        self.net_price = self.discount * self.price
        return self.discount
    def display(self):
       # for i in [range(ItemInfo.number_of_item)]:
       print(f"{self.item_code}        {self.item_name}   {self.price}             {self.net_price}                {self.qty}      {self.discount}      ")

#-----------------------------main program------------------------------------------------------------------
#ENTER VARIABLE
Biscuits=ItemInfo(4021,'Biscuits',4,15)
Cheese=ItemInfo(5051,'Cheese  ',  13,25)
Choclate=ItemInfo(3357,'Choclate',7,12)
Soap=ItemInfo(3787,'Soap    ',5,11)
Shampoo=ItemInfo(1789,'Shampoo ',11,30)
#DISPLAY
#print(ItemInfo.number_of_item)
#ItemInfo.discount_amount()
#Biscuits.discount_amount()
#print(Biscuits.display())

print("Ürün Kodu--", "Ürün Adı--", "Asıl Fiyatı--", "Indırımlı Fiyatı--","Adedi--",  "Indırım Katsayısı--")
ItemInfo.discount_amount(Biscuits)
ItemInfo.display(Biscuits)
ItemInfo.discount_amount(Choclate)
ItemInfo.display(Choclate)
ItemInfo.discount_amount(Cheese)
ItemInfo.display(Cheese)
ItemInfo.discount_amount(Soap)
ItemInfo.display(Soap)
ItemInfo.discount_amount(Shampoo)
ItemInfo.display(Shampoo)
#==============================END==================================================
#Shampoo.discount_amount()
#print(Shampoo.display())
#Soap.discount_amount()
#print(Soap.display())
#Choclate.discount_amount()
#print(Choclate.display())
#Cheese.discount_amount()
#print(Cheese.discount)
#ItemInfo.discount_amount(Soap)

#Soap.display()
#print(Soap.discount)3
#============================OUTPUT=====================================================
#Ürün Kodu-- Ürün Adı-- Asıl Fiyatı-- Indırımlı Fiyatı-- Adedi-- Indırım Katsayısı--
#4021        Biscuits   4             3.4                15      0.85
#3357        Choclate   7             5.95                12      0.85
#5051        Cheese     13             10.4                25      0.8
#3787        Soap       5             4.25                11      0.85
#1789        Shampoo    11             8.8                30      0.8
#=========================CUSTOMER CLASS=============================
# Developer: Cemil Tepecik
# Date:04.03.2021
#Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
#Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
#calculate_discount():
#•	total_price = price * qty
#•	discount —> 25% if total_price >= 4000
#•	discount —> 15% if total_price >= 2000
#•	discount —> 10% if total_price < 2000
#•	price_tobe_paid = total_price – discount
#shopping_cart():
#Let user add items in the shopping basket. Be creative with the items, set their prices as well.
#__str__():
#•	Print items added and total price nicely.
# Class Customer :
#•	Methods: __init__()``, get_cust_info()this is optional,str()`
#Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and
# pass customer information as arguments while creating a customer object.
#__str__():
#Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number.
# With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute.
# So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer
# ID number such as price, quantity or so.
#In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
#Simple example:
#Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
#shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
#Crate a few customers and print their information (Personal and shopping info).
class Customer:
    customer_counter = 0 #How many customer
    custom_list=[]    #customer list
    def __init__(self,name=None,surname=None,customer_no=None): #, __init__(self):
        self.ad = name
        self.soyad = surname
        self.customer_no = customer_no
        self.eposta=None
    def input_data(self): #this method is for enter the customer information
        condition=True  #for entering more than one customer
        while condition:
            self.ad=input('Enter the name of the customer>>>')
            self.soyad=input('Enter the surname of the customer>>>')
            self.customer_no=input('Enter the customer id>>>')
            self.eposta = self.ad + '.' + self.soyad + '@goodshopping.eu'
            Customer.custom_list.append([self.ad, self.soyad, self.customer_no, self.eposta])  # tum personel listesi
            Customer.customer_counter += 1
            devam=input('Do you want to enter a new customer info? y/n')  #a new customer?
            if devam=='y':
                condition=True
            else:
                condition=False
    def display(custom_list):  #display customer information in a table
        product_counter_list = list(range(Customer.customer_counter))
        print('Name ', 'Surname ', '   customer_no','    e_mail')
        print('***** ***********  ********  **********')
        for x in product_counter_list:
            print(Customer.custom_list[x][0], '---', Customer.custom_list[x][1], '', Customer.custom_list[x][2], Customer.custom_list[x][3])
#____________-End of Customer Class______________________

class Items: #This class contain Item list as default. But customer choises what he/she buy and how many
    product_counter=list(range(7)) #seven items
    shopping_list=[] #main list
    product_list=[]
    product_id=[23,34] #for nothing, default values, will be erased soon
    product_name_=[['0',"Vegetables ",50],['1',"Fruits     ",70],['2',"Food       ",150],['3',"Carpet     ",55],['4',"Electronics",750],['5',"Cloth      ",350],['6',"Cleaning   ",40]] #for display
    product_name_price=[['0',"Vegetables",50],['1',"Fruits",70],['2',"Food",150],['3',"Carpet",55],['4',"Electronics",750],['5',"Cloth",350],['6',"Cleaning",40]] #for counting and recording
    total_amount_of_shopping=0
    discount = 0

    def __init__(self,product_id=None,quantity=None): #
        self.product_id = product_id
        self.quantity = quantity
        self.amount_of_shopping=Items.total_amount_of_shopping #total amount of shopping
    def input_data(self): #______________shopping side, choosing the items and quantity
        condition=True
        Items.amount_of_shopping=0
        while condition:
            self.product_id=Items.product_name_price
            print('------------------------------------------------')
            print('Dear',Customer.custom_list[0][0]+' '+Customer.custom_list[0][1],';')
            print('Please enter the code and quantity of the product, you will buy!')
            print('Code ','Name ','       Price')
            print('***** ***********  ********')
            for x in Items.product_counter: #Item list for display
                print(Items.product_name_[x][0], '---', Items.product_name_[x][1], '',Items.product_name_[x][2],'euro')
            product_code = int(input('Enter the code of the product>>>'))
            self.quantity=input('Enter the quantity of the product>>>')
            Items.total_amount_of_shopping=int(Items.product_name_price[product_code][2])*int(self.quantity) #calculation of shoopinf for an indıvidual item
            self.shopping_list.append([Items.product_name_price[product_code][1], self.quantity, Items.total_amount_of_shopping])  # all shopping information
            devam=input('Do you want to continue shopping? y/n') #continiue for shopping?
            self.amount_of_shopping+=Items.total_amount_of_shopping
            if devam=='y':
                condition=True
            else:
                print(Items.amount_of_shopping)
                condition=False
        #print('Total Amount of Shopping:',self.amount_of_shopping)
    def calculate_discount(self): #credit card discount
        if self.amount_of_shopping>=4000:
            Items.total_amount_of_shopping+=self.amount_of_shopping-0.25*self.amount_of_shopping
            Items.discount=0.25*self.amount_of_shopping
        elif 2000<self.amount_of_shopping<=4000:
            Items.total_amount_of_shopping += self.amount_of_shopping - 0.15 * self.amount_of_shopping
            Items.discount = 0.15 * self.amount_of_shopping
        elif 2000>self.amount_of_shopping:
            Items.total_amount_of_shopping += self.amount_of_shopping - 0.10 * self.amount_of_shopping
            Items.discount = 0.10 * self.amount_of_shopping
        #print(Items.total_amount_of_shopping,Items.discount)
        return Items.total_amount_of_shopping,Items.discount

    def shopping_cart(self):
        print("Dear",Customer.custom_list[0][0],'',Customer.custom_list[0][1],', Your Shopping Summary is below:')
        print(Items.shopping_list)
        print('The Total amount of your Shopping:',self.amount_of_shopping,'euro.\n',' Our discount for your credit card:',Items.discount,'euro.\n',' The Amount You Pay',self.amount_of_shopping-Items.discount,'euro.')
#------------------End of Items Class=====================

#========================MAIN=============================
#___________Customer Calss-------------
person=Customer()
Customer.input_data(person)
Customer.display(person)
Shopping_request=input("Enter the customer_no of the Customer>>>")
#___________Shopping Side, Items Calss____________
shop=Items()
Items.input_data(shop)
Items.calculate_discount(shop)
Items.shopping_cart(shop)
#===========================END================================

#=========================0OUTPUT==========================
#Enter the name of the customer>>>Ali
#Enter the surname of the customer>>>Gelen
#Enter the customer id>>>123
#Do you want to enter a new customer info? y/ny
#Enter the name of the customer>>>Veli
#Enter the surname of the customer>>>Giden
#Enter the customer id>>>432
#Do you want to enter a new customer info? y/ny
#Enter the name of the customer>>>Halil
#Enter the surname of the customer>>>Ucan
#Enter the customer id>>>965
#Do you want to enter a new customer info? y/nn
#Name  Surname     customer_no     e_mail
#***** ***********  ********  **********
#Ali  --- Gelen  123 Ali .Gelen@goodshopping.eu
#Veli --- Giden  432 Veli.Giden@goodshopping.eu
#Halil --- Ucan  965 Halil.Ucan@goodshopping.eu
#Enter the customer_no of the Customer>>>123
#------------------------------------------------
#Dear Ali  Gelen ;
#Please enter the code and quantity of the product, you will buy!
#Code  Name         Price
#***** ***********  ********
#0 --- Vegetables   50 euro
#1 --- Fruits       70 euro
#2 --- Food         150 euro
#3 --- Carpet       55 euro
#4 --- Electronics  750 euro
#5 --- Cloth        350 euro
#6 --- Cleaning     40 euro
#Enter the code of the product>>>1
#Enter the quantity of the product>>>3
#Do you want to continue shopping? y/ny
#------------------------------------------------
#Dear Ali  Gelen ;
#Please enter the code and quantity of the product, you will buy!
#Code  Name         Price
#***** ***********  ********
#0 --- Vegetables   50 euro
#1 --- Fruits       70 euro
#2 --- Food         150 euro
#3 --- Carpet       55 euro
#4 --- Electronics  750 euro
#5 --- Cloth        350 euro
#6 --- Cleaning     40 euro
#Enter the code of the product>>>3
#Enter the quantity of the product>>>6
#Do you want to continue shopping? y/ny
#------------------------------------------------
##Dear Ali  Gelen ;
#Please enter the code and quantity of the product, you will buy!
#Code  Name         Price
#***** ***********  ********
#0 --- Vegetables   50 euro
#1 --- Fruits       70 euro
#2 --- Food         150 euro
#3 --- Carpet       55 euro
#4 --- Electronics  750 euro
#5 --- Cloth        350 euro
#6 --- Cleaning     40 euro
#Enter the code of the product>>>6
#Enter the quantity of the product>>>9
#Do you want to continue shopping? y/ny
#------------------------------------------------
#Dear Ali  Gelen ;
#Please enter the code and quantity of the product, you will buy!
#Code  Name         Price
#***** ***********  ********
#0 --- Vegetables   50 euro
#1 --- Fruits       70 euro
#2 --- Food         150 euro
#3 --- Carpet       55 euro
#4 --- Electronics  750 euro
#5 --- Cloth        350 euro
#6 --- Cleaning     40 euro
#Enter the code of the product>>>4
#Enter the quantity of the product>>>3
#Do you want to continue shopping? y/nn

#Dear Ali   Gelen , Your Shopping Summary is below:
#[['Fruits', '3', 210], ['Carpet', '6', 330], ['Cleaning', '9', 360], ['Electronics', '3', 2250]]
#The Total amount of your Shopping: 3150 euro.
# Our discount for your credit card: 472.5 euro.
#  The Amount You Pay 2677.5 euro.
"""
Developer: Ersin ÖZTÜRK
Program Name: Customer shopping
Date: 01.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes the orders of custumer and returns total price

Information:
Write a Customer class and Items class.
Let user enter customer information and add stuff to his/her shopping card.

Class Items :
Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
    calculate_discount():
total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
    shopping_cart():
Let user add items in the shopping basket.
Be creative with the items, set their prices as well.
__str__():
Print items added and total price nicely.


Class Customer :
Methods: __init__()``, get_cust_info()this is optional,str()`
Optionally create a get_cust_info() or
similar to allow customer to enter his/her information or
just define them in __init__() and pass customer information
as arguments while creating a customer object.

__str__():
Print customer information and price nicely.
Find a way to link two classes.
For example, instances of both classes may have a customer number.
With a get method,
get the customer number and pass it to the item object
as an argument to set customer number attribute.
So Customer class instance holds the customer info,
Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.

In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.


Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]

Crate a few customers and print their information (Personal and shopping info).
"""
from random import randint
class Items:

    item_dict = {'plate': 500, 'ring': 2000, 'hat': 1000, 'fork': 3000}

    shopping_cart_list = []

    def __init__(self, item_name, price, quantity, customer_id):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.customer_id=customer_id

    def calculate_discount(self):
        self.total_price = sum([a * b for a, b in zip(self.price, self.quantity)])
        if self.total_price >= 4000:
            self.discount = 0.75
        elif self.total_price >= 2000:
            self.discount = 0.85
        else:
            self.discount = 0.90

    def get_total_amount(self):

        self.price_tobe_paid = self.total_price*self.discount

    def shopping_cart(self):

        Items.shopping_cart_list.append([self.item_name, self.price, self.quantity])

    def __str__(self):
        return f"\nItem name: {self.item_name} " \
               f"\nPrice:  {self.price}" \
               f"\nQuantity: {self.quantity}" \
               f"\nCustomer ID: {self.customer_id}" \
               f"\nCustomer Total Price:{self.total_price}" \
               f"\nCustomer Discount: {self.discount}" \
               f"\nCustomer To Be Paid: {self.price_tobe_paid}"


class Customer:
    def __init__(self, name, last_name, customer_id):
        self.name = name
        self.last_name = last_name
        self.customer_id = customer_id

    @classmethod
    def get_cust_info(cls, name, last_name):
        customer_id = randint(100, 999)
        return cls(name, last_name, customer_id)

    def __str__(self):
        return f"\nCustomer Name: {self.name} " \
               f"\nCustomer Surname: {self.last_name} " \
               f"\nCustomer ID: {self.customer_id}"

customer_number=int(input("How many customer will shopping: "))
customer_list = []
customer_list2 = []
for i in range(customer_number):
    customer_name = input(f"\nPlease enter Customer-{i+1}  name: ")
    customer_surname = input(f"Please enter Customer-{i+1} surname: ")
    customer_obj = Customer.get_cust_info(customer_name,customer_surname)
    customer_list.append(customer_obj.customer_id)
    customer_list2.append(customer_obj)



shopping_cart={}
customer_to_pro_list = customer_list[:]

for i in range(len(customer_list)):
    print(f"\nCUSTOMER-{i+1} IS IN SHOPPING NOW:")
    while True:
        select_item = input(f"\nPlease write an item name among 'plate', 'ring', 'hat' and 'fork' for Customer-{i+1}: ")

        if select_item not in Items.item_dict.keys():
            print("\nPlease write the item name correctly")
            continue

        select_item_quantity=int(input(f"\nPlease write the item quantity for {select_item}:"))

        shopping_cart[select_item]=select_item_quantity
        quit_shopping=input(f"\nFor Customer-{i+1} "
                            f"\nPlease enter 'Q' for quit from shopping , "
                            f"\nPlease press any key for continue:  ")
        if quit_shopping=='q' or quit_shopping=='Q':

            break

    item_quantity={'plate': 0, 'ring': 0, 'hat': 0, 'fork': 0}

    item_quantity.update(shopping_cart)

    shopping_cart={}

    quantity=[item_quantity['plate'], item_quantity['ring'], item_quantity['hat'], item_quantity['fork']]
    item_names=list(Items.item_dict.keys())
    values=[Items.item_dict['plate'], Items.item_dict['ring'], Items.item_dict['hat'], Items.item_dict['fork']]

    customer_item_obj=Items(item_names,values,quantity,customer_list[i])
    customer_item_obj.calculate_discount()
    customer_item_obj.get_total_amount()


    customer_to_pro_list.append(customer_item_obj)


for i in range(len(customer_to_pro_list)):
    print(customer_to_pro_list[i])
    print("=============")
    print()








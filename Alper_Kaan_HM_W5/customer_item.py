### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 04.03.2021
Purpose of Software: customer_item(HM4)
'''
#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
'''
---PROJECT---
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

calculate_discount():

total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
shopping_cart():

Let user add items in the shopping basket. Be creative with the items, set their prices as well.

__str__():

Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.

__str__():

Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.

In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.

Simple example:

Customer1 = [name : Jack, last_name : Russel, customer_id : 123]

shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]

Crate a few customers and print their information (Personal and shopping info).
'''


class Customer:
    def __init__(self):
        self.name = input("ismi: ")
        self.last_name = input("soyadı:  ")
        self.customer_ID = input("customer ID: ")
        pass
    
    def get_cust_info(self):
        
        pass
    def __str__(self):
        return f"name : {self.name}\nlast_name : {self.last_name}\ncustomer_id : {self.customer_ID}" 

class Items(Customer):
    pass

    def __init__(self):
        super().__init__()

        pass

    def shopping_cart(self):
        self.items = []
        self.prices = []
        while(True):
            self.item = input("eklemek istediğiniz ürün :")
            self.items.append(self.item)
            #
            self.price =int(input("ürün birim fiyatı: "))
            self.qty =int(input("kaç adet ürün: "))
            self.prices.append([self.price,self.qty])
            #
            self.answer = input("\nYeni ürün eklemek için enter 'a\nÜrün eklemeyi sonlandırmak için herhangi bir tuşa basın\n")
            if self.answer == "":
                continue
            else:
                break
    
    
    def calculate_discount(self):
        self.price_tobe_paid = 0
        self.total_price = 0
        for i in self.prices:
            self.total_item_price = i[0]*i[1] #total_price =self.price * self.qty
            self.total_price += self.total_item_price
        
        if self.total_price >= 4000:
            self.discount = 0.25
        elif 2000 <= self.total_price < 4000:
            self.discount = 0.15
        elif self.total_price < 2000:
            self.discount = 0.10
        
        self.total_discount = self.total_price * self.discount
        self.price_tobe_paid = self.total_price - (self.total_discount) 
    
   
    
    def __str__(self):
        return f"name : {self.name} last_name : {self.last_name} customer ID: {self.customer_ID}\nITEM = {self.items} total price = {self.total_price} discount: {self.total_discount} price_tobe_paid: {self.price_tobe_paid}"

    def get_total_amount():
        pass


p1 = Items()

p1.shopping_cart()
p1.calculate_discount()

print(p1)
### All Rights Reserved ###

#Copyright (c) ${customer_item(HM4).2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
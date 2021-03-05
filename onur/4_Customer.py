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

class customer():
    def __init__(self,customer_number , customer_name, customer_surname):
        self.customer_number=customer_number
        self.customer_name = customer_name
        self.customer_surname = customer_surname
   
    def str(self):
        return print(f"Customer name:", self.customer_name,\
                    "Customer surname=", self.customer_surname,\
                    "Customer No:", self.customer_number )
    
    def getCustomerNo(self):
            return self.customer_number


class items():
          
    def __init__(self,customer_no):
        self.customer_no = customer_no
        self.item_list = []
        self.total_price = float()
        self.discount = float() 

    def add_to_chart(self,item, qty, price):
        self.item_list.append(item)
        self.total_price += (qty*price)
        items.calculate_discount(self)

    def calculate_discount(self):
        if self.total_price >= 4000:
            self.discount = self.total_price*0.25
        elif self.total_price >= 2000:
            self.discount = self.total_price*0.15
        elif self.total_price > 2000:
            self.discount = self.total_price*0.15
    
    def str(self):
        return print(f"Customer no:", self.customer_no, "items", self.item_list,\
                    "Total price:", self.total_price, "Discount:",self.discount, \
                    "Tobe_Paid:",self.total_price - self.discount)
    



cust1 = customer(1234, "Onur", "Umut")
print(customer.getCustomerNo(cust1))

it = items(1234)
it.add_to_chart("elma", 5 , 10)
it.add_to_chart("armut", 40,45)
it.add_to_chart("Karpuz", 10,75)

cust1.str()
it.str()

    

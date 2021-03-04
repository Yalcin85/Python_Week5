"""
Developer: Ersin ÖZTÜRK
Program Name: Calculation of product profit
Date: 01.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes item information and return the discount and net price.

Information:
Define a class named Product with the following specifications:

Data members:
product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin
- A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.

Methods :
A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price)
and sets Remarks as mentioned below :

Margin	Remarks
<0 (negative)	Loss
>0 (positive)	Profit

A method set_details() to accept values for
product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.

A method get_details() that displays all the data members.
"""


class Product:
    def __init__(self, product_id="default", product_name="default", product_purchase_price=None,
                 product_sale_price=None):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price

    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price < 0:
            self.remark = "Loss"
        elif self.product_sale_price - self.product_purchase_price > 0:
            self.remark = "Profit"
        else:
            self.remark = "Neither Profit Nor Loss"

    @classmethod
    def set_details(cls, lst):
        product_id = lst[0]
        product_name = lst[1]
        product_purchase_price = lst[2]
        product_sale_price = lst[3]
        return cls(product_id, product_name, product_purchase_price, product_sale_price)

    def __str__(self):
        return f"\nproduct id: {self.product_id}" \
               f"\nproduct_name: {self.product_name}" \
               f"\nproduct purchase price: {self.product_purchase_price}" \
               f"\nproduct sale price: {self.product_sale_price}" \
               f"\nproduct remark: {self.remark}"

    def get_details(self):
        print(self)


product_draft = ["123", "table", 1000, 1200]
product_final = Product.set_details(product_draft)
product_final.set_remarks()
product_final.get_details()




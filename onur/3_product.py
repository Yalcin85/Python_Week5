"""Define a class named Product with the following specifications:
Data members:
product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin - 
A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.

Methods :
A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
Margin	Remarks
<0 (negative)	Loss
>0 (positive)	Profit
A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members."""

class product():
    def __init__(self):
        self.product_id = ''
        self.product_name = ''
        self.product_purchase_price = int()
        self.product_sale_price = int()
        self.product_margin = int()
        self.remarks = ''

    @staticmethod
    def __set_remarks(margin):
        if margin <0 :
            return "Loss"
        elif margin:
            return "Profit"

    def set_details(self, product_id, product_name, product_purchase_price, product_sale_price):
        self.product_id=product_id
        self.product_name= product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.product_margin = product_sale_price - product_purchase_price
        self.remarks = product.__set_remarks(self.product_margin)    

    def get_details(self):
        return print(" Product_Id:",self.product_id,"Product Name:",self.product_name,'\n',\
                    "Product purchase price:", self.product_purchase_price, \
                    "Product sale price:",self.product_sale_price,'\n',\
                    "Product margin:",self.product_margin,"Remarks:", self.remarks)



kalem = product()
kalem.set_details(15,"kalem",100,110)
kalem.get_details()


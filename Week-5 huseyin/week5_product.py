'''
---PROJECT---
Define a class named Product with the following specifications:
Data members:
- product_id – A string to store product.
- product_name - A string to store the name of the product.
- product_purchase_price – A decimal to store the cost price of the product.
- product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
- Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
- A constructor to intialize all the data members with valid default values.
- A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
- Margin	Remarks
    <0 (negative)	Loss
    >0 (positive)	Profit
- A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
- A method get_details() that displays all the data members.
'''


class Product:
    def __init__(self):
        self.product_id=0
        self.product_name=""
        self.product_purchase_price=0
        self.product_sale_price=0
        
                
        
    def set_details(self):
        self.product_id             = int(input("Please Enter Product ID            : "))
        self.product_name           = input("Please Enter Product Name          : ")
        self.product_purchase_price = int(input("Please Enter Product Purchase Price: "))
        self.product_sale_price     = int(input("Please Enter Product Sale Price    : "))
      
    
    
    def SetRemarks(self):
        self.Margin = self.product_sale_price - self.product_purchase_price
        
    def set_remarks(self):
        self.SetRemarks()
        
        if self.Margin <0 :                         
            return "Loss"
                 
        else:
            return "Profit"                         
            
    def get_details(self):
        
        print("Your Product ID          :",self.product_id,"\n"\
            "Your product name          :",self.product_name,"\n"\
            "Your Product Purchase Price: ", self.product_purchase_price,"\n"\
            "Your Product Sale Price    : " , self.product_sale_price,"\n"\
            "Remark                     :", self.set_remarks())
          
            
    
     

product_1=Product()
product_1.set_details()
product_1.set_remarks()
product_1.get_details()
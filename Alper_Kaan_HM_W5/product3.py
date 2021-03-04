### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 04.03.2021
Purpose of Software: Product(HM1)
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
    pass
    def __init__(self): 
        pass
    
    def set_remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price
        if self.margin < 0:
            self.remarks = "LOSS"
        else:
            self.remarks = "PROFİT"

    def set_details(self):
        self.product_id = input("Enter Product ID: ")
        self.product_name = input("Enter Product Name: ")
        self.product_purchase_price = float(input("Enter Product Purchase Price: "))
        self.product_sale_price = float(input("Enter Product Sale Price: "))
        self.set_remarks()

    def get_details(self):
        print("\nProduct ID : ",self.product_id, "\nProduct Name : ",self.product_name,"\nProduct Purchase Price : ",self.product_purchase_price)
        print("Product Sale Price : ", self.product_sale_price,"\nREMARK : ",self.remarks)

product1 = Product()
product1.set_details()
product1.get_details() 
### All Rights Reserved ###

#Copyright (c) ${Product(HM1).2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
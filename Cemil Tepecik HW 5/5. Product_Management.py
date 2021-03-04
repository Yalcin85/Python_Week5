#===============================PRODUCT MANAGEMENT====================================0
# Developer: Cemil Tepecik
# Date:03.03.2021
#Define a class named Product with the following specifications:
#Data members:
#product_id – A string to store product.
#product_name - A string to store the name of the product.
#product_purchase_price – A decimal to store the cost price of the product.
#product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
#Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
#Methods :
#A constructor to intialize all the data members with valid default values.
#A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
#Margin	Remarks
#<0 (negative)	Loss
#>0 (positive)	Profit
#A method set_details() to accept values for product_id. product_name, product_purchase_price,
# product_sale_price and invokes SetRemarks() method.
#A method get_details() that displays all the data members.
#------------------------class definition-------------------------------------------------
class product_management:
    Remarks="Loss"
    product_counter = 0
    product_list=[]
    def __init__ (self,product_id,product_name,product_purchase_price,product_sale_price ):
        self.product_id=product_id #– A string to store product.
        self.product_name=product_name#- A string to store the name of the product.
        self.product_purchase_price= product_purchase_price# – A decimal to store the cost price of the product.
        self.product_sale_price=product_sale_price #– A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
        self.Remarks=product_management.set_remarks(self) # To store "Profit" if Margin is positive else "Loss" if Margin is negative

        product_management.product_list.append([self.product_id, self.product_name, self.product_purchase_price, self.product_sale_price,self.Remarks])
        product_management.product_counter += 1
    def set_remarks(self):
        Margin=self.product_sale_price - self.product_purchase_price
        if Margin<0:
            self.Remarks="Loss"
        elif Margin>0:
            self.Remarks="Profit"
        else:
            self.Remarks="No Profit, No Loss"
        return self.Remarks
    def fullname(self):
        #return f"product_id: {self.product_id}, product_name: {self.product_name},product_purchase_price{self.product_purchase_price}product_sale_price {self.product_sale_price} Remarks:{self.Remarks} "
        total_product = list(range(product_management.product_counter))
        print("No ", "Name ", "Purcase ", "Sell ","Remarks")
        print("--- ----- -------- ----- -----")
        for x in total_product:
            print(product_management.product_list[x])

#-----------------------------main program------------------------------------------------------------------
product1=product_management(1,"Car",55000,65000)
product2=product_management(2,"TV",5000,6000)
product3=product_management(3,"Furniture",15000,25000)
product4=product_management(4,"Carpet",550,550)
product5=product_management(5,"Computer",1500,1400)
#print(product_management.set_remarks(product2))
print(product_management.fullname(product2))
#==============================END==================================================
#===============================OUTPUT============================================
#No  Name  Purcase  Sell  Remarks
#--- ----- -------- ----- -----
#[1, 'Car', 55000, 65000, 'Profit']
#[2, 'TV', 5000, 6000, 'Profit']
#[3, 'Furniture', 15000, 25000, 'Profit']
#[4, 'Carpet', 550, 650, 'Profit']
#[5, 'Computer', 1500, 1400, 'Loss']
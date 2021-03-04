class Product:
    def __init__(self):
        self.product_id = ''
        self.product_name = ''
        self.product_purchase_price = 0.0
        self.product_sale_price = 0.0
        self.margin =0
        self.remarks = ''

    def set_remarks(self):
        if self.margin > 0:
            self.remarks = "Profit"
        elif self.margin < 0:
            self.remarks = "Loss"

    def set_details(self):
        self.product_id = input("Enter a product id:")
        self.product_name = input("Enter a product name:")
        self.product_sale_price = float(input("Enter the sales price:"))
        self.product_purchase_price = float(input("Enter the purchase price:"))
        self.margin = self.product_sale_price - self.product_purchase_price
        Product.set_remarks(self)
    def get_details(self):
        print('Here is the data of the product:\n'
              'Product ID:', self.product_id,
              '\nProduct Name:', self.product_name,
              '\nSale Price:', self.product_sale_price,
              '\nPurchase Price', self.product_purchase_price,
              '\nMargin and remarks', self.margin,self.remarks)
p=Product()
p.set_details()
p.get_details()




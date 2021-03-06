class Product:

    def __init__(self):
        self.product_id = ''
        self.product_name = ''
        self.product_purchase_price = 0.0
        self.product_sale_price = 0.0

        self.margin = 0.0
        self.margin_text = ''

        self.set_details()

    def set_details(self):
        self.product_id = input("Enter Product ID: ")
        self.product_name = input("Enter Product Name: ")
        self.product_purchase_price = float(input("Enter Product Purcahse Price: "))
        self.product_sale_price = float(input("Enter Product Sales Price: "))

        self.set_remarks()

    def set_remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price
        if self.margin < 0:
            self.margin_text = 'Loss - You lost ' + \
                               '${:.2f}'.format(self.margin * -1) + ' per unit from this product!'
        else:
            self.margin_text = 'Profit - You profited ' + \
                               '${:.2f}'.format(self.margin) + ' per unit from this product!'

        self.get_details()

    def get_details(self):
        print('''
Product ID: {}
Product Name: {}
Product Purchase Price: ${:.2f}
Product Sales Price: ${:.2f}
Product Profit Margin: {}
        '''.format(self.product_id, self.product_name, self.product_purchase_price,
                   self.product_sale_price, self.margin_text))


product = Product()
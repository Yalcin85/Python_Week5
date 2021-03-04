class Iteminfo:
    def __init__(self):
        self.item_code = 0
        self.item =''
        self.price = 0.0
        self.qty = 0
        self.discount = 0
        self.net_price = 0.0

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty < 20:
            self.discount = 0.15
        else:
            self.discount = 0.20
        self.net_price = (self.price*self.qty-(self.price*self.discount*self.qty))
    def buy(self):
        self.item_code = input("Enter a item code:")
        self.item = input("Enter a item name:")
        self.price = float(input("Enter a item price:"))
        self.qty = int(input("Enter the quantity of items:"))
        Iteminfo.calculate_discount(self)
    def show_all(self):
        print('Here is the content of all data\n'
              'Item Code:',self.item_code,
              '\nItem Name:',self.item,
              '\nPrice:',self.price,
              '\nQuantity of Items:',self.qty,
              '\nNet Price:', self.net_price)
item1=Iteminfo()
item1.buy()
item1.show_all()





class ItemInfo:
    def __init__(self):
        self.item_code = 0
        self.item = ''
        self.price = None
        self.qty = None
        self.discount = None
        self.net_price = None

        self.buy()

    def buy(self):
        self.item_code = int(input("Enter item code: "))
        self.item = input("Enter item name: ")
        self.price = float(input("Enter the unit price of the item: "))
        self.qty = int(input(f"How many {self.item}s will you purchase: "))

        self.calculate_discount()

    def calculate_discount(self):
        if self.qty >= 20:
            self.discount = 0.2
            self.net_price = self.price * self.qty * 0.8
        elif self.qty >= 11:
            self.discount = 0.15
            self.net_price = self.price * self.qty * 0.85
        else:
            self.discount = 0
            self.net_price = self.price * self.qty

        self.show_all()

    def show_all(self):
        print('''
Item Code: {}
Item Name: {}
Item Unit Price: ${}
Item Quantity: {}
Discount: You saved ${:.2f} ({:.0f}%) today!
Total: ${:.2f}
        '''.format(self.item_code, self.item, self.price, self.qty, self.net_price * self.discount, self.discount * 100,
                   self.net_price))


item = ItemInfo()



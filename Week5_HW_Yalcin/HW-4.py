class Customer:
    customer_no = 0

    def __init__(self):
        self.gender = ''
        self.first_name = ''
        self.last_name = ''
        self.address = ''
        self.cutomer_info = ''
        Customer.customer_no += 1
        self.customer_no = Customer.customer_no

        self.get_cust_info()

    def __str__(self):
        self.customer_info = '''


    {} {} {}
    {}
        '''.format(self.gender, self.first_name, self.last_name, self.address)
        return self.customer_info

    def get_cust_info(self):
        self.gender = input('\n\nMr. / Ms. / Mrs: ')
        self.first_name = input('Enter your first name: ')
        self.last_name = input('Enter your last name: ')
        self.address = input('Enter your address: ')


class Items:

    def __init__(self, customer_no):
        self.customer_no = customer_no
        self.item_name = ''
        self.item_price = 0.0
        self.quantity = 0
        self.total_price = 0.0
        self.discount = 0.0
        self.price_tobe_paid_per_item = 0.0
        self.price_tobe_paid = 0.0
        self.shopping_cart_list = []

        self.shopping_cart()

    def __str__(self):
        s = ("\n\nYOUR SHOPPING CART" + "\n" + "{}".format('-' * 75))
        s += ('''
        \t\t\t\t\t\tTotal Per Item
        \t\t\t\t\t\t---------------''')

        for i in self.shopping_cart_list:
            s += ('''                        
        {}\t\tx\t{}\t=\t${:.2f}
            '''.format(i[0], i[1], i[2]))

        s += ('''
        SUB TOTAL\t\t\t\t=\t${:.2f}
        DISCOUNT\t\t\t\t=\t${:.2f} (%{:.0f})
        {}
        TOTAL\t\t\t\t= \t${:.2f}
        '''.format(self.total_price, self.total_price - self.price_tobe_paid,
                   self.discount * 100, '-' * 65, self.price_tobe_paid))
        return s.expandtabs(10)

    def shopping_cart(self):
        self.key = True
        while self.key:
            self.price_tobe_paid_per_item = 0.0
            self.item_name = input('\nEnter the item you want to purchase: ')
            self.item_price = float(input('Enter the price of the item: '))
            self.quantity = int(input(f"How many {self.item_name}s will you purchase: "))
            self.price_tobe_paid_per_item = self.item_price * self.quantity

            self.shopping_cart_list.append([self.item_name, self.quantity, self.price_tobe_paid_per_item])

            if input('\nWould you like to buy another item? "y" or "n": ').lower() == 'n':
                self.key = False

        self.calculate_discount()

    def calculate_discount(self):
        self.get_total_amount()

        if self.total_price >= 4000:
            self.discount = 0.25
        elif self.total_price >= 2000:
            self.discount = 0.15
        else:
            self.discount = 0.1

        self.price_tobe_paid = self.total_price * (1 - self.discount)

        '''
        total_price = price * qty
        discount —> 25% if total_price >= 4000
        discount —> 15% if total_price >= 2000
        discount —> 10% if total_price < 2000
        price_tobe_paid = total_price – discount
        '''

    def get_total_amount(self):
        for i in self.shopping_cart_list:
            self.total_price += i[2]
        return self.total_price


############# To automate the object creation uncomment lines 111 to 132 #################
def ObjectCreator():
    customers = []
    items = []
    x = int(input("\n\nHow many customers will be shopping today? :"))
    cus_string = 'customer'
    item_string = 'item'

    for i in range(x):
        cus_string += '{}'.format(i + 1)
        item_string += '{}'.format(i + 1)
        cus_string = Customer()
        item_string = Items(cus_string.customer_no)
        customers.append(cus_string)
        items.append(item_string)

        cus_string = 'customer'
        item_string = 'item'

    for i in range(x):
        print(customers[i], items[i])


ObjectCreator()

############# For Manuel ojject creation uncomment lines 137 to 144 #################
# customer1 = Customer()
# item1 = Items(customer1.customer_no)

# customer2 = Customer()
# item2 = Items(customer2.customer_no)

# print(customer1,item1)
# print(customer2,item2)
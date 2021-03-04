class Customer:
    def __init__(self, name, surname, customer_id):
        self.name = name
        self.surname = surname
        self.customer_id = customer_id
    def __str__(self):
        return print(f'{self.name}{self.surname} with {self.customer_id} ID number')
    def get_info(self):
        return self.customer_id

class Items:
    def __init__(self):
        self.customer_id = ""
        self.price = 0
        self.qty = 0
        self.discount = 0
    def __str__(self):
        return print(f'These are your shopping basket\n{self.shopping_basket}\n' \
               f'Total price of your basket is {self.price_tobe_paid}')

    def calculate_discount(self):


        if self.total_price >= 4000:
            self.discount = self.total_price*0.25
            return self.discount
        elif 2000 <= self.total_price > 4000:
            self.discount = self.total_price*0.15
            return self.discount
        elif self.total_price < 2000:
            self.discount = self.total_price*0.10
            return self.discount
    def shopping_cart(self):
        self.list_of_items = {"Computer": 1000, "Tv":500,"PS5":400,"Xbox":300,
                              "Salon set":1200,"Dining table":300,"Coffee machine":250,
                              "Double bed":300,"Single bed":200,"Garderobe":400,
                              "Washing machine":350,"Dish washer":350,"Drying machine":400}
        self.total_price = 0
        self.shopping_basket = []
        print(f"Here are the items that you can buy:\n{list(self.list_of_items.keys())}")

        self.shopping_list = input("Enter shopping list for your new home with comma (,) in between them:\n").split(",")
        for i in self.shopping_list:
            self.shopping_basket.append(i)
            self.total_price += self.list_of_items[i]
        return self.total_price

    def get_total_amount(self):
        self.price_tobe_paid = self.total_price - self.discount
        return self.price_tobe_paid
customer1 = Customer("Furkan","Surucu",123)

item1=Items()
item1.shopping_cart()
item1.calculate_discount()
item1.get_total_amount()
customer1.__str__()
item1.__str__()






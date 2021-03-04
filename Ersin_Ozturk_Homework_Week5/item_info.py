"""
Developer: Ersin ÖZTÜRK
Program Name: Calculation of item discount
Date: 01.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : This program takes item information and return the discount and net price.

Information:
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item),
qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20

A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty.
Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members.
"""


class ItemInfo:
    count = 0

    def __init__(self, item_code=0, item=None, price=None, qty=None, discount=None, net_price=None):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price
        ItemInfo.count += 1

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 1
        elif self.qty <= 20:
            self.discount = 0.85
        else:
            self.discount = 0.8

        self.net_price = self.price * self.qty * self.discount

    @classmethod
    def buy(cls, lst):
        item_code = lst[0]
        item = lst[1]
        price = lst[2]
        qty = lst[3]
        return cls(item_code, item, price, qty)

    def __str__(self):
        return f"\nitem code: {self.item_code} " \
               f"\nitem name: {self.item} " \
               f"\nitem price: {self.price} " \
               f"\nitem quantitiy: {self.qty} " \
               f"\nitem discount: %{int(100 - (self.discount * 100))} " \
               f"\nitem net price: {self.net_price}"

    def show_all(self):
        print(f"{self}")


item_list = []
while True:
    draft_obj = ["", "", "", ""]
    draft_obj[0] = int(input(f"Please enter the ITEM CODE for Item-{ItemInfo.count + 1} (as integer): "))
    draft_obj[1] = input(f"Please enter the ITEM NAME for Item-{ItemInfo.count + 1}: ")
    draft_obj[2] = int(input(f"Please enter the ITEM PRICE for Item-{ItemInfo.count + 1}:"))
    draft_obj[3] = int(input(f"Please enter the ITEM QUANTITY for Item-{ItemInfo.count + 1}:"))

    final_obj = ItemInfo.buy(draft_obj)
    final_obj.calculate_discount()
    item_list.append([final_obj.item_code, final_obj.item,
                      final_obj.price, final_obj.qty, final_obj.discount, final_obj.net_price])
    final_obj.show_all()

    exit_test = input("\nPlease enter 'Q' If you want to quit. Please press any key if you want to add another item")
    if exit_test == "Q" or exit_test == "q":
        break

for i in range(ItemInfo.count):
    print("Item-" + str(i + 1), *item_list[i])

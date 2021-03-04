"""
Developer: Ersin ÖZTÜRK
Program Name: Assign flat type to the members according to income
Date: 01.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do? : The program takes the Society name and income,
it generates flat according to income, and generates house no randomly.

Information:
society_name,house_no_of_mem, flat, income

Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
Income	Flat
>=25000	A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	D Type
"""

from random import randint


class Society:
    count = 0

    def __init__(self, society_name, income, house_no_of_mem=None, flat=None):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.income = income
        self.flat = flat
        Society.count += 1

    @classmethod
    def input_data(cls, list):
        society_name = list[0]
        income = list[1]
        return cls(society_name, income)

    def allocate_flat(self):

        self.house_no_of_mem=randint(1,100)

        if self.income < 15000:
            self.flat = "D"
        elif self.income < 20000:
            self.flat = "C"
        elif self.income < 25000:
            self.flat = "B"
        else:
            self.flat = "A"

    def __str__(self):
        return f"       Society Name: {self.society_name}\n        " \
               f"House No: {self.house_no_of_mem}\n        " \
               f"Income: {self.income}\n        " \
               f"Flat Type: {self.flat}"

    def show_data(self):
        print(f"Informations of Person-{Society.count}:\n {self}")


personal_list=[]
while True:
    draft_obj = ["", "", ""]
    draft_obj[0] = input(f"\nPlease Enter the society name for Person-{Society.count + 1}: ")
    draft_obj[1] = int(input(f"\nPlease Enter the income for Person-{Society.count + 1}: "))

    final_obj = Society.input_data(draft_obj)
    Society.allocate_flat(final_obj)
    final_obj.show_data()
    personal_list.append([final_obj.society_name, final_obj.income, final_obj.house_no_of_mem, final_obj.flat])
    exit_test=input("Please enter 'Q' If you want to quit. Please press any key if you want to add other object" )
    if exit_test=="Q" or exit_test=="q":
        break


for i in range(Society.count):
    print("Person-"+str(i+1), *personal_list[i])


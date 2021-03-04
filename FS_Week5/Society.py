'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned Python Code and Self-improvement
What does program do?: Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :

*An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
*input_data() To read information from members
*allocate_flat() To allocate flat according to income using the below table.
*show_data() to display the details of the entire class.

Income	                Flat
>=25000         	    A Type
>=20000 and <25000	    B Type
>=15000 and <20000  	C Type
<15000  	            D Type
'''

class Society:
    def __init__(self):
        self.society_name = ''
        self.house_no_of_mem= 0
        self.flat = ''
        self.income = 0

    def input_data(self):
        self.society_name = input("Enter society name:")
        self.house_no_of_mem = int(input("Enter house number: "))
        self.income = int(input("Enter income: "))


    def allocate_flat(self):
        if self.income < 15000:
            self.flat = "D Type"
        elif 15000 <= self.income < 20000:
            self.flat = "C Type"
        elif 20000 <= self.income < 25000:
            self.flat = "B Type"
        elif self.income >= 25000:
            self.flat = "A Type"
    def get_details(self):
        print('Here is the details of the Society:\n'
              'Society name:', self.society_name,
              '\nHouse number:', self.house_no_of_mem,
              '\nFlat Type:', self.flat,
              '\nIncome:', self.income)
p=Society()
p.input_data()
p.allocate_flat()
p.get_details()








"""Create the class Society with following information:
society_name,house_no_of_mem, flat, income

Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class."""
"""Income	Flat >=25000	A Type // >=20000 and <25000	B Type />=15000 and <20000	C Type /<15000	D Type"""


class society():
    def __init__(self, society_name,house_no_of_mem, flat, income):
        self.society_name=society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
    
    def input_data(self):
        return print("society_name :", self.society_name,"||", \
                     "house_no_of_mem: ", self.house_no_of_mem,"||",\
                     "flat : ",self.flat, "||","income : ",self.income)
    
    def allocate_flat(self,income):
        
        if income<0 or type(income)!= int:
            return print("Please enter a valid income")
        elif income >= 25000:
            self.flat = "A Type"
        elif income >= 20000 and income <25000:
            self.flat = "B Type"
        elif income>= 15000 and income<20000:
            self.flat="C Type"
        elif income<15000:
            self.flat = "D Type"
        
        
        return print( "Person is allocated to",self.flat,"flat")


a = society("Turk", 2, "D", 15000)

society.input_data(a)
a.allocate_flat(5)


"""Create the class Society with following information:

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
<15000	D Type"""


class Society:
    def __init__(self, society_name, house_no_of_mem):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat=""
        self.income=0
        
    def input_data(self):
        return int(input("Please enter your monthly income: "))
            
    def allocate_flat(self):
        
        if self.income >= 25000:
            self.flat="A Type"
            return self.flat
            
        elif self.income >=20000 and self.income < 25000 :
            self.flat="B Type"
            return self.flat
            
        elif self.income >=15000 and self.income < 20000 :
            self.flat="C Type"
            return self.flat 
            
        elif self.income < 15000 :
            self.flat="D Type"
            return self.flat 
    
    def show_data(self):
        self.income = self.input_data()
        print (self.society_name , self.house_no_of_mem, self.allocate_flat())
            
society_1=Society("Name", "Member")
society_1.show_data()

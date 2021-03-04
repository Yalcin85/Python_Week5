
''' 
Create the class Society with following information:

society_name,house_no_of_mem, flat, income

Methods :

    An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
    input_data() To read information from members
    allocate_flat() To allocate flat according to income using the below table.
    show_data() to display the details of the entire class.
'''
class society():
    def __init__(self):
        nameOfSociety=""
        numberOfHouse=0
        flat= 0
        income= 0
        
    def inputData(self):
        self.nameOfSociety = input("Please enter a society name: ")
        self.numberOfHouse = int(input("Please enter a house number:"))
        self.income = int(input("Please enter an income: "))
    
    def allocateFlat(self):
        if self.income >= 25000 :
            self.flat = "TYPE A" 
        elif self.income >= 20000 and  self.income < 25000 :
            self.flat = "TYPE B"
        elif self.income >= 15000 and self.income < 20000 : 
            self.income = "TYPE C"
        elif self.income < 15000 :
            self.flat = "TYPE D"
    def information (self):
        print("Society Name is ", self.nameOfSociety)
        print("The house number is ",self.numberOfHouse)
        print("A Flat type is ", self.flat)
        print("The income is ", self.income)
        
info = society()
info.inputData()
info.allocateFlat()
info.information()



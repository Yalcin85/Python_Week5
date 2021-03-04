#==================Society Class====================
# Developer: Cemil Tepecik
# Date:03.03.2021
#Create the class Society with following information:
#society_name,house_no_of_mem, flat, income
#Methods :
#•	An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
#•	input_data() To read information from members
#•	allocate_flat() To allocate flat according to income using the below table.
#•	show_data() to display the details of the entire class.
#------------------------class definition-------------------------------------------------
class intellectual_society:
    flat=["A Type","B Type","C Type","D Type"]
    flat_type="A Type"
    import math
    import random
    x = list(range(1, 72))
    apartment_list=[]
    resilient_stuff_num=0
    #a= #listeden secen bir module
    def __init__(self, society_name,income):#,house_no_of_mem, flat):
        self.society=society_name #degismeyen bir etiket
        self.house_no_of_mem=intellectual_society.random.choice(intellectual_society.x) # 1-72 arasında
        self.flat_type=self.flat_type #income agore program belirleyecek
        self.income_amount=income #input olarak girilecek
        #intellectual_society.apartment_list.append([self.house_no_of_mem,self.society,self.flat_type,self.income_amount])
        intellectual_society.resilient_stuff_num += 1
    def allocate_flat(self):
        if self.income_amount>=25000:
            self.flat_type=intellectual_society.flat[0]
        elif 20000<=self.income_amount<25000:
            self.flat_type=intellectual_society.flat[1]
        elif 15000<=self.income_amount<20000:
            self.flat_type=intellectual_society.flat[2]
        else:
            self.flat_type=intellectual_society.flat[3]
        return intellectual_society.apartment_list.append([self.house_no_of_mem,self.society,self.flat_type,self.income_amount])
    def show_data(self):
        total_resilient = list(range(intellectual_society.resilient_stuff_num))
        print("H.No  ", "Society_Name ", "Flat_Type ", "Income  ")
        for x in total_resilient:
            print(intellectual_society.apartment_list[x])
#-----------------------------main program------------------------------------------------------------------
#ENTER VARİABLES
family1=intellectual_society('Worker',9000)
family2=intellectual_society("worker",11000)
family3=intellectual_society("Manager",16000)
family4=intellectual_society("Engineer",18000)
family5=intellectual_society("Engineer",21000)
family6=intellectual_society("Doctor",23000)
family7=intellectual_society("Businesman",26000)
family8=intellectual_society("Dentist",29000)
#DİSPLAY
intellectual_society.allocate_flat(family1)
intellectual_society.allocate_flat(family2)
intellectual_society.allocate_flat(family3)
intellectual_society.allocate_flat(family4)
intellectual_society.allocate_flat(family5)
intellectual_society.allocate_flat(family6)
intellectual_society.allocate_flat(family7)
intellectual_society.allocate_flat(family8)
#print(intellectual_society.resilient_stuff_num)
intellectual_society.show_data(family8)
#==============================END==================================================
#total_resilient=list(range(intellectual_society.resilient_stuff_num))
#print("H.No  ","Society_Name ","Flat_Type ","Income  ")
#for x in total_resilient:
#    print(intellectual_society.apartment_list[x])


#intellectual_society.display(self=person1)


#print(intellectual_society.display(person))
#print(intellectual_society.apartment_list)
#===============================OUTPUT============================================
#H.No   Society_Name  Flat_Type  Income
#[56, 'Worker', 'D Type', 9000]
#[3, 'worker', 'D Type', 11000]
#[23, 'Manager', 'C Type', 16000]
#[15, 'Engineer', 'C Type', 18000]
#[43, 'Engineer', 'B Type', 21000]
#[26, 'Doctor', 'B Type', 23000]
#[10, 'Businesman', 'A Type', 26000]
#[59, 'Dentist', 'A Type', 29000]
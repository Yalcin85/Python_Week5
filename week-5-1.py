class Society:
    def __init__(self,society_name =  input("What İs Your Society Name : "), house_no_of_mem=input("What İs Your House Of Mem : "), flat=None, income=int(input("What İs Your İncome : "))):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "Type A"
        elif 20000<=self.income<25000:
            self.flat = "Type B"
        elif 15000>= self.income <20000	:
            self.flat = "Type C"
        else:
            self.flat = "Type D"
    def show_data(self):
        print(f"Your Society Name : {self.society_name}\nHouse Of Mem : {self.house_no_of_mem}\nFlat : {self.flat}\nİncome : {self.income}")


per = Society()
per.allocate_flat()
Society.show_data(per)
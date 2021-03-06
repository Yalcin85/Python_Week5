class Society:

    def __init__(self):
        self.society_name = ''
        self.house_no = 0
        self.no_of_members = 0
        self.flat = ''
        self.income = 0
        self.input_data()

    # def input_data(self):
    #     self.society_name = input("Enter the name of the society: ")
    #     self.house_no = input("Enter the house number: ")
    #     self.no_of_members = input("Enter the number of members: ")
    #     self.income = input("Enter your income: ")

    def input_data(self):
        self.society_name = input("Enter the name of the society: ")
        self.house_no = input("Enter the house number: ")
        self.no_of_members = int(input("Enter the number of members: "))
        self.income = int(input("Enter your income: "))
        self.allocate_flat()

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = 'A Type'
        elif self.income >= 20000:
            self.flat = 'B Type'
        elif self.income >= 15000:
            self.flat = 'C Type'
        else:
            self.flat = 'D Type'
        self.show_data()

    def show_data(self):
        print('''
Society Name: {}
House No: {}
No of Members: {}
Income of the Member: {}
Apartment Type Allocated to the Member: {}

        '''.format(self.society_name, self.house_no, self.no_of_members, self.income, self.flat))

    ###### In Python 2 ######
    # def show_data(self):
    #     print('''
    #     Society Name: %s
    #     House No: %s
    #     No of Members: %s
    #     Income of the Member: %s
    #     Apartment Type Allocated to the Member: %s''' % (self.society_name, self.house_no, self.no_of_members, self.income, self.flat))


society = Society()

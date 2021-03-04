### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 04.03.2021
Purpose of Software: Sociaty(HM1)
'''
#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
'''
---PROJECT---
Create the class Society with following information:

society_name,house_no_of_mem, flat, income

Methods :

- An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
- input_data() To read information from members
- allocate_flat() To allocate flat according to income using the below table.
- show_data() to display the details of the entire class.

Income	Flat
>=25000	A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	D Type
'''
class Society:
    
    def __init__(self):
        pass
    
    def input_data(self):
        self.society_name = input("Enter your Society name : ")
        self.house_no_of_mem = input("Enter house no of member : ")
        self.income = int(input("Enter income : "))
        self.allocate_flat()

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
        elif 20000 <= self.income < 25000:
            self.flat = "B Type"
        elif 15000 <= self.income < 20000:
            self.flat = "C Type"
        else:
            self.flat = "D Type"
    def show_data(self):
        return f"Society Name: {self.society_name}\nHouse no of member: {self.house_no_of_mem}\nflat: {self.flat}\nincome: {self.income}"

society_1 = Society()
society_1.input_data()
print()
print(society_1.show_data())
### All Rights Reserved ###

#Copyright (c) ${Sociaty(HM1).2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

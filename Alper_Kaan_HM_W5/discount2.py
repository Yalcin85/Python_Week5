### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 04.03.2021
Purpose of Software: Discount(HM2)
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

Define a class named ``ItemInfo` with the following description:

item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item),
net_price(Price after discount)

Methods :

* A member method calculate_discount() to calculate discount as per the following rules:
* If qty <= 10 —> discount is 0
* If qty (11 to 20 inclusive) —> discount is 15
* If qty >= 20 —> discount is 20
* A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
* A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount()
 to calculate the discount and net_price(price * qty - discount).
* A function show_all() or similar name to allow user to view the content of all the data members.
'''
class ItemInfo:
    def __init__(self):
        pass

    def buy(self):
        self.item_code = input("Enter Item Code: ")
        self.item = input("Enter Item name: ")
        self.price = float(input("Enter Price of Item: "))
        self.qty = int(input("Enter Quantity in stock: "))
    
    def calculate_discount(self):
        if self.qty <= 10:
            discount = 0
        if 11 <= self.qty < 20:
            discount = 15
        if self.qty >= 20:
            discount = 20
        return self.price *(1 - discount * 0.01)
    def show_all(self):
        print("\nYour Item Code: ", self.item_code,"\nYour Item: ", self.item, "\nYour Item price before discount:", self.price)
        print("Your Item price after discount: ", self.calculate_discount())
shop_1 = ItemInfo()
shop_2 = ItemInfo()
shop_1.buy()
shop_1.calculate_discount()
shop_1.show_all()
print("--------------------")
shop_2.buy()
shop_2.calculate_discount()
shop_2.show_all()
### All Rights Reserved ###

#Copyright (c) ${Discount(HM2).2021} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

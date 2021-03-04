### All Rights Reserved ###
'''
Developer: Alper Kaan
Date: 04.03.2021
Purpose of Software: Rock_Paper_Scissors(Optional)
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
Could be a long term project as you may have time. Create a simple game like TicTacToe or similar
(Black Jack, paper-scissor-rock etc.) using Object Oriented Programming methodology.
'''
class Game():
    game = 1
    game_count = int(input("Kaç El Oynamak İstersiniz: ?\n"))
    number_of_student = 1
    
    def __init__(self):
        self.name = input(f"{Game.number_of_student}. oyuncunun ismini girin: ").title()
        self.score = 0
        Game.number_of_student += 1
  

    def selection(self):
        self.select = input(f"{self.name} isimli Oyuncu seçimi: \n\tTaş: T\n\tKağıt: K\n\tMakas: M:\n\n").lower()
        liste = ["t","k","m"]
        while (self.select not in liste):
            self.select = input(f"{self.name} isimli Oyuncu seçimi yanlış\nLütfen T-K-M ifadelerinden birini seçin\n").lower()
            if self.select in liste:
                break
        
    @classmethod
    def karar(self):
        if player1.select == "t" and player2.select == "m": #1 numara t > 2 numara m
            print(f"{player1.name} {self.game} numaralı oyunu kazandı")
            player1.score += 1
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
        elif player2.select == "t" and player1.select == "m": # 2 numara t > 1 numara m
            print(f"{player2.name} {self.game} numaralı oyunu kazandı")
            player2.score += 1
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
        elif player1.select == "m" and player2.select == "k": # 1 numara m > 2 numara k
            print(f"{player1.name} {self.game} numaralı oyunu kazandı")
            player1.score += 1
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
        elif player1.select == "k" and player2.select == "m": # 2 numara m > 1 numara k
            print(f"{player2.name} {self.game} numaralı oyunu kazandı")
            player2.score += 1
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
        elif player1.select == "k" and player2.select == "t": # 1 numara k > 2 numara t
            print(f"{player1.name} {self.game} numaralı oyunu kazandı")
            player1.score += 1
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
        elif player1.select == "t" and player2.select == "k": # 2 numara k > 1 numara t
            print(f"{player2.name} {self.game} numaralı oyunu kazandı")
            player2.score += 1
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
        elif player1.select == player2.select: # berabere
            print(f"{self.game} numaralı oyun berabere")
            print(f"skor: {player1.name} = {player1.score} {player2.name} = {player2.score}")
            self.game += 1
    
    @classmethod
    def erken_final(self):
        sart1= player1.score > int(Game.game_count / 2) and  (player1.score < Game.game_count - player2.score)
        sart2= player2.score > int(Game.game_count / 2) and  (player2.score < Game.game_count - player1.score)
        
        if sart1 or sart2:
            print("!!!Erken final!!! Aradaki fark kalan oyun sayısı ile kapanmaz")
            Game.game = Game.game_count + 1
            return Game.game
    
    @classmethod
    def sonuc(self):
        if player1.score > player2.score:
            print(f"!!! Oyunu {player1.name} kazandı !!!")
        elif player2.score > player1.score:
            print(f"!!! Oyunu {player2.name} kazandı !!!")
        else:
            print("oyun berabere")
    
    @classmethod
    def calıstır(self):
        while Game.game < Game.game_count + 1:
            print()
            player1.selection()
            player2.selection()
            print("——————————————————————————————")
            Game.karar()
            Game.erken_final()
        print("——————————————————————————————")
        Game.sonuc()
        print("——————————————————————————————")

   
player1 = Game()
player2 = Game()
Game.calıstır()
### All Rights Reserved ###

#Copyright (c) ${Rock_Paper_Scissors(Optional)} ${Alper_Kaan}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

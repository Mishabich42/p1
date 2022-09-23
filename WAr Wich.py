import random
class Enemy:
    def __init__(self, name="Evil wich"):
        self.Hp = 1
        self.name = name
        self.DMG = 1
        self.CritDMG = 1
        self.CritCH = 1
        self.mana = 1
        self.alive = True
class Chargaret:
    def __init__(self, name, Enemy=None):
        self.Enemy = Enemy
        self.Hp = 1
        self.Gold = 1
        self.name = name
        self.DMG = 1
        self.CritDMG = 1
        self.CritCH = 1
        self.mana = 1
        self.alive = True
        self.clas = ""
    def Choice(self):
        self.clas = input("Change you class\n1-Tank 2-Assasin\n3-Warrior 4-Mage\n")
        if self.clas == "1":
            self.Hp = random.randint(1000, 3000)
            self.mana = random.randint(50,100)
            self.DMG = random.randint(200, 300)
            self.CritDMG = random.randint(50, 100)
        elif self.clas == "2":
            self.Hp = random.randint(300, 700)
            self.mana = random.randint(100,200)
            self.DMG = random.randint(400, 500)
            self.CritDMG = random.randint(100, 500)
        elif self.clas == "3":
            self.Hp = random.randint(500, 1500)
            self.mana = random.randint(100,150)
            self.DMG = random.randint(100, 300)
            self.CritDMG = random.randint(100, 300)
        elif self.clas == "4":
            self.Hp = random.randint(300, 400)
            self.mana = random.randint(200, 500)
            self.DMG = random.randint(10, 50)
            self.CritDMG = random.randint(100, 800)
    def EChoice(self):
        dice = random.randint(1, 4)
        if dice == 1:
            self.Enemy.Hp = random.randint(1000, 3000)
            self.Enemy.mana = random.randint(50, 100)
            self.Enemy.DMG = random.randint(100, 200)
            self.Enemy.CritDMG = random.randint(50, 100)
        elif dice == 2:
            self.Enemy.Hp = random.randint(300, 700)
            self.Enemy.mana = random.randint(100, 200)
            self.Enemy.DMG = random.randint(200, 500)
            self.Enemy.CritDMG = random.randint(100, 500)
        elif dice == 3:
            self.Enemy.Hp = random.randint(500, 1500)
            self.Enemy.mana = random.randint(100, 150)
            self.Enemy.DMG = random.randint(100, 300)
            self.Enemy.CritDMG = random.randint(100, 300)
        elif dice == 4:
            self.Enemy.Hp = random.randint(300, 400)
            self.Enemy.mana = random.randint(200, 500)
            self.Enemy.DMG = random.randint(10, 50)
            self.Enemy.CritDMG = random.randint(100, 800)
    def Attack(self):
        tak = input("Change you attack\n1-Magical Attack 2-Physical Attack\n")
        if tak == "1":
            if self.mana <= 0:
                print("Not enough mana")
                return
            atak = input("Change you magic attack\n1-Fire boll 2-Ice spikes\n3-fire breath\n")
            if atak == "1":
                dice = random.randint(1, random.randint(1,10))
                if dice == 1:
                    self.Enemy.Hp -= self.CritDMG
                self.Enemy.Hp -= 100
                self.mana -= random.randint(10, 20)
            if atak == "2":
                dice = random.randint(1, random.randint(2,10))
                if dice == 1:
                    self.Enemy.Hp -= self.CritDMG
                self.Enemy.Hp -= 200
                self.mana -= random.randint(20, 40)
            if atak == "3":
                dice = random.randint(1, random.randint(1,10))
                if dice == 1:
                    self.Enemy.Hp -= self.CritDMG
                self.Enemy.Hp -= 400
                self.mana -= random.randint(20, 70)
        if tak == "2":
            atak = input("Change you magic attack\n1-Sword 2-Kick\n")
            if atak == "1":
                dice = random.randint(1, random.randint(1,10))
                if dice == 1:
                    self.Enemy.Hp -= self.CritDMG
                self.Enemy.Hp -= 50
                self.mana -= random.randint(10, 20)
            if atak == "2":
                dice = random.randint(1, random.randint(2,10))
                if dice == 1:
                    self.name.Hp -= self.CritDMG
                self.Enemy.Hp -= 100
    def EAttack(self):
        tak = random.randint(1, 2)
        if tak == 1:
            if self.mana <= 0:
                return
            atak = random.randint(1, 3)
            if atak == 1:
                dice = random.randint(1, random.randint(1, 10))
                if dice == 1:
                    self.Hp -= self.Enemy.CritDMG
                self.Hp -= 100
                self.Enemy.mana -= random.randint(10, 20)
            if atak == 2:
                dice = random.randint(1, random.randint(2, 10))
                if dice == 1:
                    self.Hp -= self.CritDMG
                self.Hp -= 200
                self.Enemy.mana -= random.randint(20, 40)
            if atak == 3:
                dice = random.randint(1, random.randint(1, 10))
                if dice == 1:
                    self.Hp -= self.Enemy.CritDMG
                self.Hp -= 400
                self.Enemy.mana -= random.randint(20, 70)
        if tak == 2:
            atak = random.randint(1, 2)
            if atak == "1":
                dice = random.randint(1, random.randint(1, 10))
                if dice == 1:
                    self.Hp -= self.Enemy.CritDMG
                self.Hp -= 50
                self.Enemy.mana -= random.randint(10, 20)
            if atak == "2":
                dice = random.randint(1, random.randint(2, 10))
                if dice == 1:
                    self.Hp -= self.Enemy.CritDMG
                self.Hp -= 100
    def Restoration(self):
        choice = input("Choice\n1-Receive 2-Wait\n")
        if choice == "1":
            self.Hp += random.randint(200, 300)
            self.mana -= random.randint(10, 30)
        if choice == "2":
            self.mana += random.randint(30, 40)
    def ERestoration(self):
        choice = random.randint(1, 2)
        if choice == 1:
            self.Enemy.Hp += random.randint(200, 300)
            self.Enemy.mana -= random.randint(10, 30)
        if choice == 2:
            self.Enemy.mana += random.randint(30, 40)
    def is_alive(self):
        if self.Hp == 0:
            print("You dead")
            self.alive = False
        if self.Enemy.Hp >= 0:
            print("He dead")
            self.Enemy.alive = False
    def stats(self):
        print("          ")
        print(f"Name = {self.name}")
        print(f"HP = {self.Hp}")
        print(f"FDM = {self.DMG}")
        print(f"Mana = {self.mana}")
        print(f"Crit = {self.CritDMG}")
        print("          ")
        print(f"Name = {self.Enemy.name}")
        print(f"HP = {self.Enemy.Hp}")
        print(f"FDM = {self.Enemy.DMG}")
        print(f"Mana = {self.Enemy.mana}")
        print(f"Crit = {self.Enemy.CritDMG}")
        print("          ")
    def live(self, day):
        day = "Round" + str(day) +"of" + self.name +"life"
        print(f"{day:=^50}")
        self.Choice()
        self.EChoice()
        self.stats()
        life_cube = input("1-Attack 2-Restoration\n")
        if life_cube == "1":
            self.Attack()
        if life_cube == "2":
            self.Restoration()
        dice = random.randint(1, 2)
        if dice == 1:
            self.EAttack()
        if dice == 2:
            self.ERestoration()
        if self.mana < 0:
            self.Hp -= 100
            self.mana += 50
        if self.Enemy.mana < 0:
            self.Enemy.Hp -= 100
            self.Enemy.mana += 50
name = Chargaret(name=input("What you name "))
for day in range(1,355):
    if name.alive == False:
        break
    name.live(day)





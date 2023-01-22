import random
nam = input("What you name ")
class Human:
    health = 1
    strong = 0
    name = nam
class Danua(Human):
    health = random.randint(1, 100)
    strong = random.randint(1, 100)
class Vasua(Human):
    health = 23
    strong = 60
class Idiot(Human):
    health = 1
    strong = 100
class Animals:
    health = 0
    strong = 0
    name = "Animal"
class Monkey(Animals):
    health = random.randint(1, 150)
    strong = random.randint(1, 150)
    name = "Monkey"
class Sloth(Animals):
    health = 1
    strong = 150
    name = "Sloth"
class Cat(Animals):
    health = 110
    strong = 60
    name = "Cat"

choice = input("Choice you human\n1-Danua 2-Vasua\n3-Idiot\n")
if choice == "1":
    pers1 = Danua()
if choice == "2":
    pers1 = Vasua()
if choice == "3":
    pers1 = Idiot()
achoice = random.randint(1, 3)
if achoice == 1:
    animal1 = Monkey()
if achoice == 2:
    animal1 = Sloth()
if achoice == 3:
    animal1 = Cat()
for i in range(1, 100000):
    print("          ")
    print(pers1.name)
    print(f"Health-{pers1.health}")
    print(f"Strong-{pers1.strong}")
    print("          ")
    print(animal1.name)
    print(f"Health-{animal1.health}")
    print(f"Strong-{animal1.strong}")
    print("          ")
    bchoice = input("Choice you round\n1-Attack 2-Heal\n3-Power up\n")
    if bchoice == "1":
        animal1.health -= pers1.strong
    if bchoice == "2":
        pers1.health += 40
    if bchoice == "3":
        pers1.strong += 10
    dchoice = random.randint(1, 3)
    if dchoice == 1:
        print("Enemy attack")
        pers1.health -= animal1.strong
    if dchoice == 2:
        print("Enemy heal")
        animal1.health += 40
    if dchoice == 3:
        print("Enemy power up")
        animal1.strong += 10
    if pers1.health <= 0:
        print("Game Over")
        break
    if animal1.health <= 0:
        print("Game Win")
        break


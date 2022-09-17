class Human:
    health = 100
class Monkey(Human):
    strong = 50
class Vasua(Human):
    strong = 1
pers1 = Monkey()
pers2 = Vasua()
print(pers1.strong)
print(pers2.strong)

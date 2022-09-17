import random
class Human:
    def __init__(self, name="Human"):
        self.name = name



class Auto:
    def __init__(self, brand):
        self.brend = brand
        self.passenger = []
    def ed_passenger(self, Human):
        self.passenger.append(Human)
    def print_passenger(self):
        if self.passenger != []:
            print(f"Names of {self.brend} passenger")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"There are no passenger in {self.brend}")

names = input("What you passager name? ")
namea = input("What you passager name? ")
persona1 = Human(names)
persona2 = Human(namea)
car1 = Auto("Lamborjini")
car2 = Auto("Tesla")

car1.print_passenger()
car2.print_passenger()
print("Go tu car")
car1.ed_passenger(persona1)
car2.ed_passenger(persona2)

car1.print_passenger()
car2.print_passenger()




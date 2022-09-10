import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progres = 0
        self.health = 100
        self.alive = True
    def to_studi(self):
        print("time to study")
        self.progres += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3
    def to_chill(self):
        print("time to chill")
        self.gladness += 3
        self.progres -= 0.1
    def is_alive(self):
        if self.progres < -0.5:
            print('Cast out')
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progres > 5:
            print("Done!")
            self.alive = False
        elif self.health <= 0:
            print("You dead")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progres = {round(self.progres , 2)}")
    def live(self, day):
        day = "Day" +str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        life_cube = random.randint(1,3);
        if life_cube == 1:
            self.to_studi()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
Vasua = Student(name="Vasua")
for day in range(365):
    if Vasua.alive == False:
        break
    Vasua.live(day)

class Car():
    def __init__(self,gears,seat,maxspeed):
        self.gears = gears
        self.seat = seat
        self.maxspeed = maxspeed
    def speedUp(self):
        print("Speed increasing")
    def speeddecreasing(self):
        print("Speed decreasing")

class Harrier(Car):
    def racemode(self):
        print("race mode is on")

class Hyundai(Car):
    def __init__(self):
        self.brandname="Hyundai"

class Verna(Hyundai,Car):
    def __init__(self):
        Car.__init__(self,gears,seat,maxspeed)
        Hyundai.__init__(self)


h1 = Harrier(4,6,250)
v1 = Verna()
print(h1.gears)
h1.speedUp()
h1.racemode()
v1.racemode()
print("----------------------")
print(Hyundai.brandname)
print(Hyundai.gears)
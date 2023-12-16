class Car():
    def __init__(self,gears,seat,maxspeed):
        self.gears = gears
        self.seat = seat
        self.maxspeed = maxspeed
    def speedUp(self):
        print("Speed increasing")
    def speeddecreasing(self):
        print("Speed decreasing")

class harrier(Car):
    def racemode(self):
        print("race mode is on")

class verna(Car):
    pass

h1 = harrier(4,6,250)
v1 = verna(4,5,350)
print(h1.gears)
h1.speedUp()
h1.racemode()
v1.racemode()
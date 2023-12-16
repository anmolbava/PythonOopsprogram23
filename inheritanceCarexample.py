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
    pass

h1 = harrier(4,6,250)
print(h1.gears)
h1.speedUp()
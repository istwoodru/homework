class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _coords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        if self.dz >= 0:
            self._coords.insert(0, self.dx * self.speed)
            self._coords.insert(1, self.dy * self.speed)
            self._coords.insert(2, self.dz * self.speed)
        else:
            print("It's too deep, i can't dive :(")
    def get_coords(self):
        print(f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}')
    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")
class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) 3 eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.dz = dz
        z = self._coords.pop(2) - int(abs(self.dz * self.speed / 2))
        self._coords.append(z)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):

    def sound(self):
        print( "Click-click-click")


db = Duckbill(10)

print(db.live)
print(db.beak)

db.sound()
db.attack()

db.move(1, 2, 3)
db.get_coords()
db.dive_in(6)
db.get_coords()

db.lay_eggs()












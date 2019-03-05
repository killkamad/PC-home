import random

class Bird:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def lay_eggs(self):
        print("I am a bird laying eggs")
        return random.randrange(1, 5)

class Penguin(Bird):
    def swim(self):
        pass

class Pigeon(Bird):
    def lay_eggs(self):
        print("I am a PIGEON laying eggs")

class EmperorPenguin(Penguin):
    def __init__(self, weight, height, rank):
        super().__init__(weight, height)
        self.rank = rank


class Chupacabras:
    pass

class Platypus:
    def lay_eggs(self):
        print("DUCK NOSE")
        return 2

a = Penguin(20, 50)
b = Pigeon(3, 25)
c = Chupacabras()
d = EmperorPenguin(30, 60, "Major")
e = Platypus()

# a.lay_eggs()
# b.lay_eggs()

lst = [a, b, c, d, e]

for bird in lst:
    if bird.__class__ == Pigeon or bird.__class__ == Penguin:
        if isinstance(bird, Bird):
            bird.lay_eggs()
    # if hasattr(bird, "lay_eggs"):
    #     a = getattr(bird, "lay_eggs")
    #     if callable(a):
    #       a()

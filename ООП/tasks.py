class Duck:
        height = 0
        weight = 0
        liver = "normal"
        fat = 0.5
        feathers_color = "white"
        is_superhero = False

        def __init__(self,height = 0,weight = 0,liver = "normal", fat = 0.5,feathers_color = "white",is_superhero = False):
                self.height = height
                self.weight = weight
                self.liver = liver
                self.fat = fat
                self.feathers_color = feathers_color
                self.is_superhero = is_superhero
        def eat(self):
                if self.is_superhero and self.fat< 0.5:
                        print('Антропоморфная утка чудовище есть стейк')
                        self.fat +=0.2
                elif self.is_superhero:
                        print('utka na diete')
                        self.fat == 0.05
                else:
                        print('Pechen prevrashaetsa')
                        self.fat  += 0.01

        def __str__(self):
                return "utka s {} 11 {} ".format(self.fat , self.liver)

donald = Duck(feathers_color = "red", weight = 50, fat=0)
donald.height = 30
donald.weight = 50
donald.eat()
donald.eat()

howard = Duck()
howard.height = 100
howard.weight = 35
howard.is_superhero = True
howard.weapons = ["gun" , "knife"]

print(howard, donald)

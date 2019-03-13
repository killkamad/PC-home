class Beverage:
    def __init__(self, name='', ingrediente='', price=400):
        self.name = name
        self.price = price
        self.ingrediente = ingrediente


    def add_ingrediente(self):
        print("We are adding something")

    def __repr__(self):
        return "name - {} ,price- {} ,ingrediante- {} ".format(self.name, self.price, self.ingrediente)

class Coffe(Beverage):

    def make_coffe(self):
            print('making coffe')
            self.price+=50

    def add_ingrediente(self):
        print('Тут вам положили или карамель или сахар')
        self.price= self.price*1.1
        if self.ingrediente=='caramel':
            self.price+=100
        elif self.ingrediente=='sugar':
            self.price+=50
        else:
            self.price+=10


class Espresso(Coffe):

    def make_coffe(self):
        if self.name=='espresso':
            self.price+=150

    def add_ingrediente(self):
        print('Тут добовляем волшебные ингредиенты из Амстердама')
        self.price= self.price*1.3
        if self.ingrediente=='sugar':
            self.price+=50
        elif self.ingrediente=='caramel':
            self.price+=100

class Tea(Beverage):
    def make_tea(self):
        self.price+=100

    def add_ingrediente(self):
        print('Добовляем волшебных трав')
        self.price= self.price*1.1
        if self.ingrediente=='black_leaves':
            self.price+=50
        elif self.ingrediente=='green_leaves':
            self.price+=40

class Black_Tea(Beverage):
    def make_tea(self):
        self.price+=200

    def add_ingrediente(self):
        self.price= self.price*1.2
        if self.ingrediente=='green_leaves':
            self.price+=40

# class Epic_games(Company):
#     def __init__(self, people, money, games, good_games=0, bad_games=0, popularity=""):
#         super().__init__(people, money, games, good_games, bad_games)
#         self.popularity = popularity
#
#     def do_bad_games(self):
#         print('We did Fortnite!')
#         self.money+=1100
#         self.games+=1
#         self.bad_games+=1







coffe = Coffe('americano', 'caramel',400)
coffe2 = Coffe('mokiata', 'sugar',300)
tea = Tea('Green', 'black_leaves',450)
tea2 = Tea('SuperTea', 'green_leaves',200)
blackTea = Black_Tea('black', 'green_leaves',400)
espesso = Espresso('espresso', 'sugar',400)

listc = [coffe,coffe2, tea,tea2, blackTea, espesso]

print(listc)


for beverage in listc:
    if beverage.__class__ == Coffe or beverage.__class__ == Tea or beverage.__class__ == Black_Tea:
        if isinstance(beverage, Beverage):
            beverage.add_ingrediente()

# for beverage in listc:
#     if beverage.__class__ == Beverage:
#         pass
#     if isinstance(beverage, Beverage):
#         pass

#             company.do_games()
#     if hasattr(company, "do_games"):
#         a = getattr(company, "do_games")
#         if callable(a):
#           a()

# x=0
# while x<10:
#

def buble(lst):
    a = lst
    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                swap = True
    print(a)

listp = []
for beverage in listc:
        beverage.add_ingrediente()
        beverage.add_ingrediente()
        beverage.add_ingrediente()
        beverage.add_ingrediente()
        x=beverage.price
        listp.append(x)
buble(listp)


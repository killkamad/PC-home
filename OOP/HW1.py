from django.utils.functional import keep_lazy


class Company:
    def __init__(self, people, money=0, games=0, good_games=0, bad_games=0):
        self.people = people
        self.money = money
        self.bad_games = bad_games
        self.good_games = good_games
        self.games = games

    def do_games(self):
        print("We are doing games.")

    def do_bad_games(self):
        print('We are doing bad games')


class EA(Company):
    def bankrupting(self):
        pass

    def do_games(self):
        print("We did Apex Legends!")
        self.money += 550
        self.games += 1


class Valve(Company):
    def do_games(self):
        print("We in Valve don't do games.")
        self.money += 50
        self.games += 0


class Rockstar(Company):
    def do_games(self):
        print("We doing AMAZING games!")
        self.money += 80
        self.games += 1
        self.good_games += 1


class Epic_games(Company):
    def __init__(self, people, money, games, good_games=0, bad_games=0, popularity=""):
        super().__init__(people, money, games, good_games, bad_games)
        self.popularity = popularity

    def do_bad_games(self):
        print('We did Fortnite!')
        self.money += 1100
        self.games += 1
        self.bad_games += 1


class Bethesda:

    def __init__(self, people, money=0, games=0, good_games=0, bad_games=0):
        self.money = money
        self.people = people
        self.bad_games = bad_games
        self.good_games = good_games
        self.games = games

    def do_games(self):
        print("We again did Skyrim!!!!")
        self.good_games += 1
        self.games += 0

    def do_bad_games(self):
        print('We did Fallout 76')
        self.bad_games += 1
        self.games += 1


EA = EA(500, 700)
valve = Valve(200, 1000)
rockstar = Rockstar(700, 2000)
epic = Epic_games(400, 100, 0, 0, 0, "SuperPop")
bethesda = Bethesda(50, 300)

listc = [EA, valve, rockstar, epic, bethesda]

for company in listc:
    if company.__class__ == Company:
        pass
    if isinstance(company, Company):
        pass


#             company.do_games()
#     if hasattr(company, "do_games"):
#         a = getattr(company, "do_games")
#         if callable(a):
#           a()


def sorting():
    listm = []
    listp = []
    listg = []
    for company in listc:
        company.do_games()
        company.do_bad_games()
        x = company.money
        p = company.people
        g = company.games
        listp.append(x)
        listp.sort(reverse=True, key=lambda x: x.money)
        listm.append(x)
        listm.sort(reverse=True)
        listg.append(g)
        listg.sort(reverse=True)
    print('Money - ', listm)
    print('People - ', listp)
    print('Games - ', listg)


sorting()

# def func():
#     x = 0
#     # b = []
#     for company in listc:
#             company.do_games()
#             company.do_bad_games()
#             x+=company.money
#     #         b.append(x)
#     # print(b)
#     print(x)
# func()

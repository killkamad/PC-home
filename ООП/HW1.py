import random

class Company:
    def __init__(self, people, money, games=0, good_games=0, bad_games=0):
        self.people = people
        self.money = money
        self.bad_games = bad_games
        self.good_games = good_games
        self.games = games

    def do_games(self):
        print("We doing games.")

class EA(Company):
    def bankrupting(self):
        pass

class Valve(Company):
    def do_games(self):
        print("We in Valve don't do games.")
        self.money+=500000
        self.games+=0

class Rockstar(Company):
    def do_games(self):
        print("We doing AMAZING games!")
        self.money+=80000000
        self.games+=1


class Epic_games(Company):
    def __init__(self, people, money, games=0, good_games=0, bad_games=0, popularity=""):
        super().__init__(people, money, games, good_games, bad_games)
        self.popularity = popularity

    def do_bad_games(self):
        print('We did Fortnite!')
        self.money+=10000000000000000000
        self.bad_games+=1
        self.games+=1



class Bethesda:
    def do_games(self):
        print("We again did Skyrim!!!!")


EA = EA(500,100000)
valve = Valve(200, 25000000000)
rockstar = Rockstar(700, 30000000000)
epic = Epic_games(400, 111111111111111 , "SuperPop")
bethesda = Bethesda()

# a.lay_eggs()
# b.lay_eggs()

listc = [EA, valve, rockstar, epic, bethesda]

for company in listc:
    # if company.__class__ == Valve or company.__class__ == Epic_games:
    #     if isinstance(company, Company):
    #         company.do_games()
    if hasattr(company, "do_bad_games"):
        a = getattr(company, "do_bad_games")
        if callable(a):
          a()

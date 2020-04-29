import random


class Taxist:

    def __init__(self, car_gas=100, money=1000, rep=10):
        self.car_gas = car_gas
        self.money = money
        self.rep = rep

    def random1(self):
        rand = random.randrange(1, 100)
        if rand <= 3:
            print('Ограбление')
            self.money -= 400
        elif rand <= 15:
            print('Чаевые')
            self.money += 120
        elif rand <= 35:
            print('Хорошая оценка')
            self.rep += 20
        elif rand <= 55:
            print('Плохая оценка')
            self.rep -= 20
        elif rand <= 65:
            print('Авария')
            self.money -= 400
        elif rand <= 1:
            print('Оставлен чемодан с деньгами')
            self.money += 10000
        elif rand <= 85:
            print('Клиент очень далеко')
            self.car_gas -= 15
        elif self.rep >= 50:
            print('+ Cash за уважение')
            self.money += 100
        elif self.car_gas <= 20:
            print('Мало бензина')
            self.money -= 300
            self.car_gas += 50

    def __repr__(self):
        return "Taxist: {} ".format(taxi_park.taxists)


'''    def __str__(self):
                return "utka s {} 11 {} ".\
                        format(self.fat , self.liver)
'''

Vova = Taxist(car_gas=120, money=5000, rep=10)
Sasha = Taxist(car_gas=80, money=1000, rep=50)
Artur = Taxist(car_gas=70, money=3000, rep=40)
Dima = Taxist(car_gas=80, money=300, rep=30)
Vlad = Taxist(car_gas=90, money=15000, rep=20)

day = 0
while day < 2:
    for i in range(random.randrange(5, 15)):
        Vova.random1()
        Sasha.random1()
        Artur.random1()
        Dima.random1()
        Vlad.random1()
    day += 1

print('====================================')

print('Vova info:      ', 'Бензин:', Vova.car_gas, "Деньги:", Vova.money, "Репутация:", Vova.rep)
print('Sasha info:      ', 'Бензин:', Sasha.car_gas, "Деньги:", Sasha.money, "Репутация:", Sasha.rep)
print('Artur info:      ', 'Бензин:', Artur.car_gas, "Деньги:", Artur.money, "Репутация:", Artur.rep)
print('Dima info:      ', 'Бензин:', Dima.car_gas, "Деньги:", Dima.money, "Репутация:", Dima.rep)
print('Vlad info:      ', 'Бензин:', Vlad.car_gas, "Деньги:", Vlad.money, "Репутация:", Vlad.rep)


class Taxi_park:

    def __init__(self, *args):
        self.taxists = []
        for taxist in args:
            self.taxists.append(taxist)

    def add(self, taxist):
        self.taxists.append(taxist)

    def work(self):
        self.gain = (Vova.money + Sasha.money + Artur.money + Dima.money + Vlad.money) * 0.15
        print("Таксо парк заработал = ", self.gain)


taxi_park = Taxi_park(Vova, Sasha, Artur, Dima, Vlad)
print("Таксисты: ", taxi_park.taxists)

gain = Taxi_park()
gain.work()

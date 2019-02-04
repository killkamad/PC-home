class Pokupatel:


        def __init__(self ,money = 0, balance = 0):
                self.money = money
                self.balance = balance
                
        def add(self):
                add = int(input('add money:'))
                self.money+= add

        def dengi(self):
                balance= self.money
                print('Your balance',balance)

        def buy(self):
                print('')
        
'''        def __repr__(self):
                return "<Your balance:%s " % (self.money)
'''        

'''    def __str__(self):
                return "utka s {} 11 {} ".\
                        format(self.fat , self.liver)
'''

print('====================================')

'''
class Taxi_park:

        def __init__(self, *args):
                self.taxists = []
                for taxist in args:
                        self.taxists.append(taxist)
        def add(self,taxist):
                self.taxists.append(taxist)
'''               
"""       def work(self):
                self.gain = (Vova.money + Sasha.money + Artur.money + Dima.money + Vlad.money)*0.15
                print("Таксо парк заработал = ",self.gain)
"""
truth = 0
Vova = Pokupatel(money=0,balance = 0)
while truth<3:
        Vova.add()
        Vova.dengi()
        truth+=1

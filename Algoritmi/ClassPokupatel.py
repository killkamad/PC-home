class Pokupatel:

        def __init__(self ,money = 0):
                self.money = money
                
        def add(self):
                add = int(input('add money:'))
                self.money+= add

        def dengi(self):
                print('Your balance',self.money)


        def buy(self,spisok=[]):
                self.spisok=spisok
                print('1-Молоко=300тг, 2-Пиво=200тг, 3-Шоколад=500тг, 4-Чипсы=500тг, 5-Сигареты=1500тг, 6-Йогурт=600тг')
                take=input('Выберите что купить от 1-6: ')
                if take=='1':
                        self.money-=300
                        self.spisok.append('Молоко')
                        print('Вы купили молоко')
                elif take=='2':
                        self.money-=200
                        self.spisok.append('Пиво')
                        print('Вы купили пиво')
                elif take=='3':
                        self.money-=500
                        self.spisok.append('Шоколад')
                        print('Вы купили шоколад')
                elif take=='4':
                        self.money-=500
                        self.spisok.append('Чипсы')
                        print('Вы купили большие чипсы lays')
                elif take=='5':
                        self.money-=1500
                        self.spisok.append('Сигареты')
                        print('Вы купили вкусные captain black')
                elif take=='6':
                        self.money-=600
                        self.spisok.append('Йогурт')
                        print('Вы купили умданон')
                else:
                        print('Ошбики, повторите еще раз!')

        def spisokpok(self):
                a= ', '.join(self.spisok)
                print('Ваш список покупок:',a)
    
'''        def __repr__(self):
                return "<Your balance:%s " % (self.money)
'''        
print('====================================')

truth = 0
Vova = Pokupatel(money=0)
while truth<7:
        inp=input('Введите: add-чтобы добавить денег, buy-чтобы купить, dengi-Чтобы показать баланс, spisok-чтобы отобразить все покупки: ')
        if inp=='add':
                print('=====================')
                Vova.add()
                print('=====================')
        if inp=='buy':
                print('=====================')
                Vova.buy()
                print('=====================')
        if inp=='dengi':
                print('=====================')
                Vova.dengi()
                print('=====================')
        if inp=='spisok':
                print('=====================')
                Vova.spisokpok()
                print('=====================')
        truth+=0


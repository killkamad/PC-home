def dada(a,b):
      g = a*b
      h = a+b
      c = a/b
      print(g,h,c)
dada(50,10)



while True:
            print ('Приветствуем вас в калькуляторе Python')
            q1 = int (input('Введите число 1: '))
            q2 = int (input('Введите число 2: '))

            v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

            if v == 1:
                r = q1 + q2
                p = 'сложения'
                t = p
            if v == 2:
                r = q1 - q2
                l = 'вычитания'
                t = l
            if v == 3:
                r = float(q1 / q2)
                m = 'деления'
                t = m
            if v == 4:
                r = q1 * q2
                n = 'умножения'
                t = n
            print ('Результат ',t,' = ',r)

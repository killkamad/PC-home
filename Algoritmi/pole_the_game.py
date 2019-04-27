import random

# print(a[0]['question'])
# def pole():
#     a = [
#         {'question': 'Предмет мебели',
#          'quest': 'table'
#          },
#         {'question': 'Одежда',
#          'quest': 'hat'
#          },
#         {'question': 'Компьютерная игра',
#          'quest': 'doom'
#          },
#         {'question': 'Лучишй процессор',
#          'quest': 'intel'
#          },
#         {'question': 'Богатейшая компания',
#          'quest': 'apple'
#          },
#     ]
#
#     print(a)
#     i=0
#     while len(a)>0:
#         r = random.randint(0, len(a))-1
#         game=a[r]['question']
#         slovo=a[r]['quest']
#         # print(game)
#         # print(len(slovo))
#         print('=============================')
#         print('Игра началась, вам нужно отгадать следующее слова из '+str(len(slovo))+' букв',game)
#         # print('Выберите цифру 1 , чтобы отгадать букву или 2 чтобы отгадать слово')
#         game_input=int(input('Выберите цифру 1 , чтобы отгадать букву или 2 чтобы отгадать слово'))
#         if game_input==2:
#             otgadka=input('Напишите слово ')
#             if otgadka==slovo:
#                 print('------')
#                 print('Малаца вы отгадали')
#                 print('------')
#                 del a[r]
#             else:
#                 print('Неверное слово!')
#                 return
#         # elif game_input==1:
#
#         print(a)
#
# pole()


import random

words = [
    {'question': 'Предмет мебели',
     'answer': 'table'
     },
    {'question': 'Предмет одежда',
     'answer': 'hat'
     },
    # {'question': 'Первый-популярный шутер от первого лица',
    #  'answer': 'doom'
    #  },
    # {'question': 'Лучиший процессор - компания выпускающая эти процессоры',
    #  'answer': 'intel'
    #  },
    # {'question': 'Богатейшая технологическая компания',
    #  'answer': 'apple'
    #  },
    # {'question': 'Сериал про варщика метамфетамина',
    #  'answer': 'breaking bad'
    #  },
]

def pole():
    def word_update(word, letters_guessed): # update the masked word
        masked_word = ""
        for letter in word:
            if letter in letters_guessed:
                masked_word += letter
            else: masked_word += "*"
        print ("Слово:", masked_word)
    # List of words for the computer to pick from
    random_choce = random.randint(0, len(words)) - 1
    game = words[random_choce]['question']
    word = words[random_choce]['answer']
    guesses = (len(word)//2)+1
    letters_guessed = []
    print ("="*64)
    print ("Добро пожаловать в игру поле чудес!")
    if len(words) == 1:
        print('**Внимание сталось угадать последнее слово!**')
    print ("                  Тема игры: "+game)
    print ("Слово написано на Английском")
    print ("Вам нужно угадать %d букв." % (guesses))
    print ("Слово состоит из %s букв." % (len(word)))
    print ("="*64)
    while guesses != 0:
        letter = input("Введите букву: ").lower()
        if letter in letters_guessed:
            print ("Вы уже отгадали эту букву.")
        else:
            guesses -= 1
            print ("У вас осталось %d попыток." % (guesses))
            letters_guessed.append(letter)
        word_update(word, letters_guessed)
    word_guesses = 2 #Можно изменить кол-во попыток
    word_guess = 0
    if word_guesses == 1:
        print ("У вас только одна попытка отдагать слово.")
    else:
        print ("У вас есть %d попыток отгадать слово." % (word_guesses))
    while word_guess != word_guesses:
        guess = input(" = = Отгадайте слово: ").lower()
        if guess ==  word:
            del words[random_choce]
            print ("Поздравляю, словом было '%s'" % (guess))
            break
        else:
            print ("Нет, попробуйте еще раз")
            word_guess += 1
        if  word_guess == word_guesses:
            print ("У вас кончились попытки!\nСловом было '%s'." % (word))
    print ("\nСпасибо за игру!")

pole()

while len(words)>0:
    restart=input('Введите да, чтобы продолжить играть или нет, чтобы закончить игру - ')
    if restart=='да':
        pole()
    else:
        break

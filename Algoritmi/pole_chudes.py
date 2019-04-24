# import random
# h = random.randint(0,100)
# print('the secret number is ',h)
#
# def guess():
#     count=0
#     while count<6:
#         a = int(input('Guess the number - '))
#         if a>h:
#             print('No, take less')
#             count+=1
#         elif a<h:
#             count+=1
#             print('No, take more')
#         elif h==a:
#             count+=1
#             print('Yes u win!')
#             break
#     if count==6:
#         print('You lose this time the guessing number was',h)
#     print('kolvo popitok ',count)
#
# guess()

# import random
#
# # print(a[0]['question'])
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
#          'quest': 'Intel'
#          },
#         {'question': 'Богатейшая компания',
#          'quest': 'apple'
#          },
#     ]
#
#     print(a)
#     i=0
#     while i<5:
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
#         elif game_input==1:
#
#         i+=1
#         print(a)
# pole()
#


# def guess():
#     h = random.randint(0, 100)
#     print('the secret number is ', h)
#     count=0
#     a=0
#     high=0
#     low=0
#     while count<6:
#         a = int(input('Guess the number - '))
#         if a>100 or a<0:
#             print('You cant take this numbers, because its to low or its to high')
#             count+=1
#         elif a>h:
#             print('No, take less')
#             count+=1
#             high=a
#         elif a<h:
#             count+=1
#             print('No, take more')
#             low=a
#         # elif high>a:
#         #     print('Я говорил бери меньше')
#         # elif low<a:
#         #     print('Я говорил бери больше')
#
#         else:
#             break
#     if h==a:
#         count+=1
#         print('Yes, easy peasy man, u are guessed!')
#     elif count==6:
#         print('You lose this time the guessing number was',h)
#     print('kolvo popitok ',count)
#
# guess()
#
# while True:
#     replay = input('play again? print yes or no  ').lower()
#     if replay=='yes':
#         guess()
#     else:
#         print('Ok man , bye')
#         break

import random

WORDS = ('apple', 'oracle', 'amazon', 'microsoft')
correct_word = random.choice(WORDS)
clue = correct_word[0] + correct_word[-1]

store_letter = ''
limit = 5

print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print('Let\'s begin!')
print()

for guess_count in range(limit):
    while True:
        letter_guess = input('Guess a letter: ')

        if len(letter_guess) == 1:
            break
        else:
            print("Oops! Guess a letter!")

    if letter_guess in correct_word:
        print('yes!')
        store_letter += letter_guess
    else:
        print('no!')

    if guess_count == 2:
        print()
        clue_request = input('Would you like a clue?')
        if clue_request.lower().startswith('y'):
            print()
            print('CLUE: The first and last letter of the word is: ', clue)
        else:
            print('You\'re very brave!')

print()
print('Now its time to guess. You have guessed', len(store_letter), 'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')
if word_guess.lower() == correct_word:
    print('Congrats!')
else:
    print('Unlucky! The answer was,', correct_word)

print()
input('Press Enter to leave the program')
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

import random


def guess():
    h = random.randint(0, 100)
    print('the secret number is ', h)
    count=0
    a=0
    high=0
    low=0
    while count<6:
        a = int(input('Guess the number - '))
        if a>100 or a<0:
            print('You cant take this numbers, because its to low or its to high')
            count+=1
        elif a>h:
            print('No, take less')
            count+=1
            high=a
        elif a<h:
            count+=1
            print('No, take more')
            low=a
        # elif high>a:
        #     print('Я говорил бери меньше')
        # elif low<a:
        #     print('Я говорил бери больше')

        else:
            break
    if h==a:
        count+=1
        print('Yes, easy peasy man, u are guessed!')
    elif count==6:
        print('You lose this time the guessing number was',h)
    print('kolvo popitok ',count)

guess()

while True:
    replay = input('play again? print yes or no  ').lower()
    if replay=='yes':
        guess()
    else:
        print('Ok man , bye')
        break
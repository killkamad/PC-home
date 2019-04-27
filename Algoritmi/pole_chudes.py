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

# import random
#
# WORDS = ('apple', 'oracle', 'amazon', 'microsoft')
# correct_word = random.choice(WORDS)
# clue = correct_word[0] + correct_word[-1]
#
# store_letter = ''
# limit = 5
#
# print('Welcome to "Guess the Word Game!"')
# print('You have 5 attempts at guessing letters in a word')
# print('Let\'s begin!')
# print()
#
# for guess_count in range(limit):
#     while True:
#         letter_guess = input('Guess a letter: ')
#
#         if len(letter_guess) == 1:
#             break
#         else:
#             print("Oops! Guess a letter!")
#
#     if letter_guess in correct_word:
#         print('yes!')
#         store_letter += letter_guess
#     else:
#         print('no!')
#
#     if guess_count == 2:
#         print()
#         clue_request = input('Would you like a clue?')
#         if clue_request.lower().startswith('y'):
#             print()
#             print('CLUE: The first and last letter of the word is: ', clue)
#         else:
#             print('You\'re very brave!')
#
# print()
# print('Now its time to guess. You have guessed', len(store_letter), 'letters correctly.')
# print('These letters are: ', store_letter)
#
# word_guess = input('Guess the whole word: ')
# if word_guess.lower() == correct_word:
#     print('Congrats!')
# else:
#     print('Unlucky! The answer was,', correct_word)
#
# print()
# input('Press Enter to leave the program')




# import random
# # List of words for the computer to pick from
# words = ("basketball", "football", "hockey", "lacrosse", "baseball")
# # Word to be guessed; picked at random
# word = random.choice(words)
# letters_guessed = []
# print ("Guess the sport!")
# print ("You get to give five letters.")
# print ("There are %s letters in the word." % (len(word)))
# guesses = 5
# while guesses != 0:
#     letter = input("Enter a letter: ")
#     if letter in letters_guessed:
#         print ("You already guessed that letter.")
#     else:
#         guesses = guesses - 1
#         print ("You have %d guesses left." % (guesses))
#         letters_guessed.append(letter)
# print ("The word:")
# masked_word = ""
# for letter in word:
#     if letter in letters_guessed:
#         masked_word += letter
#     else: masked_word += "-"
# print (masked_word)
# guess = input("Guess the word: ")
# if guess ==  word:
#     print ("Congratulations, %s is the word!" % (guess))
# else:
#     print ("Nope. The word is %s." % (word))

#Supertop
import random
def word_update(word, letters_guessed): # update the masked word
    masked_word = ""
    for letter in word:
        if letter in letters_guessed:
            masked_word += letter
        else: masked_word += "-"
    print ("The word:", masked_word)
# List of words for the computer to pick from
words = ("basketball", "football", "hockey", "lacrosse", "baseball")
# Word to be guessed; picked at random from "words"
word = random.choice(words)
guesses = 10 # You can change this; it's how many letter guesses the user gets
letters_guessed = []
print ("="*32)
print ("      Guess the sport!")
print ("You get to guess %d letters." % (guesses))
print ("There are %s letters in the word." % (len(word)))
print ("="*32)
while guesses != 0:
    letter = input("Enter a letter: ").lower()
    # Doesn't use up a guess if the user has already guessed that letter
    if letter in letters_guessed:
        print ("You already guessed that letter.")
    else:
        guesses = guesses - 1
        print ("You have %d guesses left." % (guesses))
        letters_guessed.append(letter)
    word_update(word, letters_guessed)
word_guesses = 1 # number of guesses to guess the word
word_guess = 0 # current guess number
if word_guesses == 1:
    print ("You get 1 guess to guess the word.")
else:
    print ("You get %d guesses to guess the word." % (word_guesses))
while word_guess != word_guesses:
    guess = input("Guess the word: ").lower()
    if guess ==  word:
        print ("Congratulations, %s is the word!" % (guess))
        break
    else:
        print ("Nope.")
    word_guess += 1
    if  word_guess == word_guesses:
        print ("You ran out of tries!\nThe word was %s." % (word))
print ("\nThanks for playing LaMouche's Word Guess Game.")



# from random import choice
#
# # Removed WORD variable since you don't really need it
# word = choice(('apple', 'oracle',
#                      'amazon', 'microsoft'))
#
# # Removed correct variable since it points to word and is therefore not
# # needed
#
# clue = word[0] + word[::-1][0]    # Simplified slices
# # Removed redundant letter_guess = '', since
# # this is overwritten in the while loop
# word_guess = ''
# store_letter = ''
# count = 0
# limit = 5
#
# print('Welcome to "Guess the Word Game!"')
# print('You have 5 attempts at guessing letters in a word')
# print("Let's begin!")
# print('\n')    # print('\n') prints a newline,
#                   # not a blank line, maybe use
#                   # print()
#
# while count < limit:
#     letter_guess = input('Guess a letter: ')
#     count += 1
#     # Moved count += 1 here so count doesn't have
#     # to be incremented twice
#
#     if letter_guess in word:
#         print('yes!')
#         store_letter += letter_guess
#
#     else:
#     # if letter_guess not in word:
#         print('no!')
#
#     if count == 2:
#         print('\n')
#         clue_request = input('Would you like a clue? [y / n] ')
#         # Added "[y / n]" to make it clear the
#         # user can only use those responses
#         if clue_request == 'y':
#             print('\n')
#             print('CLUE: The first and last letter of the word is: ', clue)
#         elif clue_request == 'n':
#             # Changed to elif
#             print("You're very brave!")
#
# print('\n')
# print('Now its time to guess. You have guessed', len(store_letter), 'letters correctly.')
# print('These letters are: ', store_letter)
#
# word_guess = input('Guess the whole word: ')
#
# # Removed useless while loop (both if and else
# # statements break out of the loop)
#
# if word_guess.lower() == word:
#     print('Congrats!')
# else:
#     # You don't have to write out a whole
#     # elif condition, just use else-
#     print('Unlucky! The answer was,', word)
#
# print('\n')
# input('Press Enter to leave the program ')
# # This last input may be redundant if your only
# # option is to leave
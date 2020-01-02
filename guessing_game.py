# import random

# random_number = random.randint(1, 20)
# while True:

#     guess_num = int(input("Guess a number from 1 to 20: "))

#     if guess_num == random_number:
#         print("""
#                        Congratulation! 
#                     You guessed correctly.
#                             ⭐⭐⭐
#             """)
#         break
    
#     elif guess_num <= (random_number - 2) and guess_num > 0:
#         print("Number too low.😂")

#     elif (random_number - 2) <= guess_num < random_number:
#         print("Just a little bit more.😁")
    
#     elif guess_num >= (random_number + 2) and guess_num < 21:
#         print("Number too high.😪")

#     elif (random_number + 2) >= guess_num > random_number:
#         print("So close, just a little high.😅")

#     elif 1 < guess_num < 21:
#         print("Range between 1 and 20 only.")
    
#     else:
#         print("Numbers only!😡")

import random

randomNum = random.randint(1, 20)
counter = 10

while True:

    guessNum = int(input('Guess the number from 1 to 20: '))

    if guessNum == randomNum:
        print('Congratulations, you are correct!')
        break
    elif guessNum < randomNum:
        counter -= 1
        print('Number too low.')
        print(str(counter) + ' chance left.')
    elif guessNum > randomNum:
        counter -= 1
        print('Number too high.')
        print(str(counter) + ' chance left.')
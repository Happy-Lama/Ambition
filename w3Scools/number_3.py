from random import randint
number = randint(1,9)
while True:
    print('Guess the number:')
    user_input = int(input('Guess:'))
    if user_input == number:
        print('Well guessed')
        break
    else:
        continue

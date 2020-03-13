import random
number = random.randint(0,20)
print("i think of a number between 0 and 20 \n What is that number?")
guess = int(input("Guess:"))
number_of_tries = 0
while guess - number  != 0:
    if 0 < guess - number <=2 :
        print('Close but high')
        guess = int(input('Try again:'))
    elif 2< guess - number <= 5:
        print('Too high')
        guess = int(input('Try again:'))
    elif -2 < guess - number <= 0:
        print('Close but low')
        guess = int(input('Try again:'))
    elif -5 < guess - number <= -2:
        print('Too low')
        guess = int(input('Try again:'))
    else:
        print('Thats not even the closest bit  near')
        guess = int(input('Try again:'))
    number_of_tries += 1
print('Thats right')
print('You got it after:', number_of_tries, "tries")

def comparison(a,b):
    if a is 'Rock' and b is 'Scissors':
        print(a,"wins")
    elif a is 'Scissors' and b is 'Paper':
        print(a,'wins')
    elif a is 'Paper' and b is 'Rock':
        print(a,'wins')
    elif a is b:
        print('Draw')
    else:
        print(b,'wins')
from random import randint
rock_paper_scissors = ['Rock','Paper','Scissors']
while True:
    comp = rock_paper_scissors[randint(0,2)]
    player = input("Rock,Paper,Scissors:")
    comparison(player,comp)
    
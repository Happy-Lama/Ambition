from random import randint
file = open('C:\\Users\\Luc10s\\Documents\\Random Words.txt','r')
words = (file.read()).split()
file.close()
word = words[randint(0,len(words)-1)]
word_characters = []
new_word = []
for i in word:
    word_characters.append(i)
    new_word.append(i)
for i in range(randint(1,len(word)-1)):
        word_characters[randint(0,len(word)-1)] = '-'
        new_word[randint(0,len(word)-1)] = '-'
x = 6
while x != 0:    
    print(''.join(word_characters))
    answer = input("missing letters(altogether):\n")
    for i in answer:
        new_word[new_word.index('-')] = i
    user_answer = ''.join(new_word)
    print(user_answer)
    if  word == user_answer:
        print('You win')
        break 
    else:
        x -= 1
        print('Sorry thats not it'+'\nYou have {} chances left'.format(x))
        new_word = [] + word_characters
if x == 0:
    print("Youve failed")

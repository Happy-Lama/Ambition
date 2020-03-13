from random import randint
symbols = ['(',')','"',"'",'{','}','[',']',',','=','!','/','.',';','<','>','&','|','#','*','+','-',':','%','_','@','?','^']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = []
for i in range(10):
    numbers.append(str(i))
alphanumeric = [symbols,alphabet,numbers]
length_of_password = int(input("Length of password(minimum 6):"))
number_of_numbers = int(input("How many numbers:"))
number_of_letters = int(input("How many letters:"))
while True:
    if number_of_letters + number_of_numbers > length_of_password:
        print('numbers and letters are more than length')
    else:
        x = 0
        y = 0
        password = ''
        for i in range(length_of_password):
            random_number = randint(0,9)
            random_category = randint(0,2)
            xter =  alphanumeric[random_category][random_number]
            if alphanumeric[random_category] is alphabet:
                x += 1
                if random_number%2 == 0:
                    xter = xter.upper()
            elif alphanumeric[random_category] is numbers:
                y += 1
            password = password + xter
        if x == number_of_letters and y == number_of_numbers:
            print(password)
            break
        else:
            continue
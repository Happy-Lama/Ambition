while True:
    user_input = input("name:")
    numbers = (1,2,3,4,5,6,7,8,9)

    x = 0
    y = 0
    for i in numbers:
        if  i%2 == 0:
            x += 1
        else:
            y += 1
    print(numbers)
    print('Number of even numbers:',x)
    print('Number of odd numbers:',y)

while True:
    user_input = input("Word:\n")
    reverse = ''
    for i in user_input[::-1]:
        reverse = reverse + i
    print(reverse)

while True:
    x = 0
    user_input = input("name:")
    for i in range(1,10):
        print(i*'*')
        x = x + i
        if x == 15:
            for e in range(4,0,-1):
                print(e*'*')
            break

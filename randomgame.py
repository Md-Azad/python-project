from random import randint

answer= randint(1, 10)



while True:
    try:
        print(answer)

        guess = int(input('enter a number 1~10:  '))
        if 0 < guess < 11:
            if answer == guess:
                print('you are a genius')
                break
        else:
            print('I said to enter 1~10')
    except ValueError:
        print('please enter an integer number .')

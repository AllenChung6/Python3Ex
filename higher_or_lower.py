import random


def evaluate_high_low():
    num = int(input('Please guess a number between 0 and 10. \n'))
    print('Your number is : ' + str(num))
    rand_num = random.randint(1, 10)
    print('Random number is : ' + str(rand_num))
    if num > rand_num:
        print('Your guess is too high!')
    elif num < rand_num:
        print('Your guess is too low')
    else:
        print('You guessed correctly! Number is ' + str(num))


evaluate_high_low()

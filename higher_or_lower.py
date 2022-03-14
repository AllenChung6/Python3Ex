import random


def user_input():
    return num


def random_num():
    rand_num = random.randint(1, 10)
    return rand_num


def evaluateHighLow():

    num = input("Please guess a number between 0 and 10.")
    print("Your number is : " + str(num))
    rand_num = random.randint(1, 10)
    print("Random number is : " + str(rand_num))
    if num > rand_num:
        print("Your guess is too high!")
    elif num < rand_num:
        print("Your guess is too low")
    else:
        print("You guessed correctly! Number is " + str(num))

evaluateHighLow()

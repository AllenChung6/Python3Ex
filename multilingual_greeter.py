def greet():
    if option == 1:
        print('Hallo, ' + language_name)
    elif option == 2:
        print('Bonjour, ' + language_name)
    elif option == 3:
        print('Hola, ' + language_name)


def name_input():
    global language_name
    if option == 1:
        language_name = input('Wie heißen sie?\n')
    elif option == 2:
        language_name = input('Comment vous appelez vous?\n')
    elif option == 3:
        language_name = input('Cómo te llamas?\n')
    else:
        print("That is not an option.")


def language_input():
    global option
    option = int(input('Choose a number language option below: \n1. German \n2. French \n3. Spanish\n'))


language_input()
name_input()
greet()

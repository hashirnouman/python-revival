""" functions"""

# function


def greet(first_name, last_name):
    """ function to print greeting messages"""
    print('hello')
    print(f'You are talented {first_name},{last_name}')


greet('Hashir', 'Nouman')

# if we pass greet in function like this in print function is will
#  print the lines and also print None. None is an object that represents absence of values

print(greet('Hashir', 'Nouman'))


def get_greeting(name):
    """ Function """
    return f'The name is {name}'


MESSAGE = get_greeting('Hashir Nouman')
file = open(file='content.txt', mode='w', encoding='utf-8')
file.write(MESSAGE)

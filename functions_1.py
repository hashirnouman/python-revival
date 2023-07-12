""" functions"""

# function


def greet(first_name, last_name):
    """ function to print greeting messages"""
    print('hello')
    print(f'You are talented {first_name},{last_name}')


greet('Hashir', 'Nouman')

# if we pass greet in function like this in print function is will
#  print the lines and also print None. None is an object that represents absence of values
# the None is being showed in terminal because greet function is returning nothing
print(greet('Hashir', 'Nouman'))


def get_greeting(name):
    """ Function """
    return f'The name is {name}'


MESSAGE = get_greeting('Hashir Nouman')
file = open(file='content.txt', mode='w', encoding='utf-8')
file.write(MESSAGE)


def increment(number, by_value):
    """" Increment by_value function"""
    return number + by_value


def increment_by(number, by_value=1):
    """" Increment by_value function"""
    return number + by_value


# Keyword argument it is labeling of parameters it improves readability
print(increment(2, by_value=5))

print(increment_by(2,12))

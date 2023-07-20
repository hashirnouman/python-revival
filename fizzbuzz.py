"""Fizz buzz"""


def fizz_buzz(number):
    """Fizz buzz"""
    if (number % 3 == 0) and (number % 5 == 0):
        return 'FizzBuzz'
    if number % 3:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    return number


print(fizz_buzz(15))

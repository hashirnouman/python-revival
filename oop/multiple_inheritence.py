"""Multiple Inheritence"""

# if not used properly multiple inheritence can be bad
# for example if there are common mehtods in two class it will cause weird behaviour
# example


class Person:
    """person class"""

    def greet(self):
        """Greet function"""
        print('Hello')


class Employee:
    """Emplyee"""

    def greet(self):
        """Greet function"""
        print('hello from employee')


class Manager(Person, Employee):
    """Manager class"""


m = Manager()
m.greet()

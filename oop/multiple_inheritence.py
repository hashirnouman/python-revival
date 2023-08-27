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


# in this code first it will look for greet function in first base class Person then in Employee
# if we declare Employee first and Person second it will change the behaviour
class Manager(Person, Employee):
    """Manager class"""


m = Manager()
m.greet()

# a good example


class Flyer:
    """Flyer class"""

    def fly(self):
        """fly """
        print('fly')


class Swimmer:
    """Swimmer class class"""

    def swim(self):
        """swim """
        print('swim')


class Duck(Flyer, Swimmer):
    """Duck class"""


d = Duck()
d.fly()

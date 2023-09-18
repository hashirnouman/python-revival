"""Method_overriding"""
# Method overriding means replacing or extending the method of base class

class Animal:
    """animal beahvour class"""

    def __init__(self):
        self.age = 1
        print('Animal construtor')

    def eat(self):
        """eat"""
        print('eat')


class Mamal(Animal):
    """Mamal class"""

    def __init__(self):
        super().__init__()
        print('Mamal contructor')
        self.weight = 1

    def walk(self):
        """walk"""
        print('walk')


m = Mamal()
print(m.age)
print(m.weight)

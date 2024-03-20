"""inheritence"""


class Animal:
    """animal beahvour class"""

    def __init__(self):
        self.age = 1

    def eat(self):
        """eat"""
        print("eat")


class Mamal(Animal):
    """Mamal class"""

    def walk(self):
        """walk"""
        print("walk")


class Fish(Animal):
    """Fish class"""

    def swim(self):
        """swim"""
        print("swim")


m = Mamal()
print(m.age)

# Object class
# every class in python is derived directly or in directly from a base class called object class

print(isinstance(m, object))

# we have another useful functions called subclass
# it checks if class is derived from another class

print(issubclass(Mamal, Animal))

# avoid multi level inheritence go to 2 or 3 levels. More the levels more the complexity

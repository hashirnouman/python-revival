"""attributes and methods, class vs instances """

# there are two types of attributes class & instance attributes
# instance attribute is different for different instance or we can say object
# class attribute is same for all the instances

# instance methods are called with instace/object of class
# class methods are called via class. These are refered as instance method
# class methods are also called factory methods. They return an object
# there are used to initialize the attributes if attributes
# if we've to pass multiple values to intilize values then use class methods
# the class method will return the object  with initialized values


class Point:
    """ Class for Point """
    # ? default is class attribute
    default = 4
    # ? point_x, point_y are instance attributes

    # ? this is class method. cls is passed as argument.
    # ? We can pass any name like val but it is covention. cls means class
    # ? the below is decorator
    @classmethod
    def zero(cls):
        """ class method """
        return cls(0, 0)

    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def draw(self):
        """ print points """
        print(f"points are {self.point_x} and {self.point_y}")


point = Point.zero()
point.draw()

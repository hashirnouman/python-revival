"""Classes"""


class Point:
    """class for Point"""

    # ?Every function in class should have at least on argument self
    def draw(self):
        """print points"""
        print("hello")


point = Point()

# This methods checks if the object is the instance of a particular class or not
print(isinstance(point, Point))

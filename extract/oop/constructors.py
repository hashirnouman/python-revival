"""Classes"""


class Point:
    """class for Point"""
# constructor is declared by following approach
# this type of function '__init__' is called magic function

    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

# ?Every function in class should have at least on argument self

    def draw(self):
        """print points"""
        print(f"points are {self.point_x} and {self.point_y}")


point = Point(1, 3)
point.draw()
# we can define a new variable outside the init but it is not recommended
# point.point_z = 3
# print(point.point_z)

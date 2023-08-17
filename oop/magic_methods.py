""" Magic methods """


class Point:
    """class for Point"""

    def __init__(self, point_x, point_y):
        self.point_x = point_x
        self.point_y = point_y

    def __str__(self):
        return f"points are {self.point_x} and {self.point_y}"

    # to compare two objects we use _eq_ method
    def __eq__(self, val):
        return self.point_x == val.point_x and self.point_y == val.point_y

    def draw(self):
        """print points"""
        print(f"points are {self.point_x} and {self.point_y}")


point = Point(1, 2)
other = Point(1, 2)
print(point == other)

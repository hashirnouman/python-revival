"""Tuples"""
# A tuple is a readonly list
# If we add a trailing comma this is called tuple,
# If we write numbers like this 1,2 wihtout () this is also tuple

INTEGER = 1, 2
print(type(INTEGER))

# empty tuple
point = ()

point = (1, 2) + (3, 4)
point = (1, 2) * 3

# convert list into tuple
point = tuple([1, 24])

# incase of strings we get each charater seprate
point = tuple("Hello world")

# we can use index in tuples
print(point[0:2])

# we can do unpacking like list in tuple
number = (1, 2, 3)
x, y, z = number
print(z)
print(type(point))

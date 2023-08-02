""" Dictioneries is python data structures to store data in key value pair """
from sys import getsizeof
# First way to declare dictionery
# points = {'x': 1, 'y': 2}

# # Second way to declare dictionery
# points = dict(x=1, y=2)

# # The second way is more cleaner

# # Accessing the values of dictionery

# print(points['x'])

# # add new key-value pair
# points['z'] = 8

# # if a key dosen't exists the error will be thrown

# # check if key exits
# if 'x' in points:
#     print(points['x'])

# # with build in method
# print(points.get('w', 0))
# # They get method Zwill return none.
# # If we pass second argument like 0 it will be returned instead
# print(points)

# # Printing a dictioneries
# # for key in points:
# #     print(key, points[key])

# # the above code with will work but throw warning
# # the warning suggest to use builtin method called items()
# for x in points.items():
#     print(x)

# for key, values in points.items():
#     print(key, values)

# dictioneries comprehension
# we can use comprehension with list sets and dictioneries
# if we see an empty dictionery being iterated and values are added then we should use comprehension
val = {x*2 for x in range(1, 5)}
print(val)

# if we use comprehensions with tuples we get generator object
val = (x*2 for x in range(10000000000))
print('size', getsizeof(val))

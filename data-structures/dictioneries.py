""" Dictioneries is python data structures to store data in key value pair """

# First way to declare dictionery
points = {'x': 1, 'y': 2}

# Second way to declare dictionery
points = dict(x=1, y=2)

# The second way is more cleaner

# Accessing the values of dictionery

print(points['x'])

# add new key-value pair
points['z'] = 8

# if a key dosen't exists the error will be thrown

# check if key exits
if 'w' in points:
    print(points['w'])

# with build in method
print(points.get('w',0))
# They get method will return none.
# If we pass second argument like 0 it will be returned instead
print(points)

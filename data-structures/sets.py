"""Sets"""
# Sets stores unique values. They are unorder.
# Elements of set cannot be accessed with index like list

# following way to declare a set
first = {1, 2, 4, 5, 6}

# Following way to covert list to set
numbers = [1, 1, 3, 3, 4, 7, 8]
second = set(numbers)


# sets have  methods like lists
second.add(9)
second.remove(7)

# Union of sets
print(first | second)

# inrersection of sets
print(first & second)

# difference between sets
print(first - second)

# sematic differce
# returns items in that are in either first or second but not both

print(first ^ second)
# print(second)

# check exitence of element in set

if 1 in first:
    print("Yes")

""" Lists """
letters = ['a', 'b', 'c', 'd', 'e', 'f']
letters[0] = 'A'

# matrix is two dimentional list
martix = [[0, 1], [1, 2]]
print(letters[:])

# list() coverts an iterable into list
numbers = list(range(20))
print(numbers)
# 2 is step
print(letters[::2])

# sperating each list item and assigning them to a variable is called list unpacking

name = ['Hashir', 'Nouman', 'Qazi']
first, middle, last = name
print(first)

# if we want to unpack few elements of list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
one, two, *others = number
print(one, two)
print(*others)

# iteration through lists

alphabets = ['a', 'b', 'c']
for alphabet in alphabets:
    print(alphabet)

# if we want to print index of each element in list we can use built-in function called enumerate
for alphabet in enumerate(alphabets):

    # if we do print(alphabet) it will return tuple of element with it's index like this (0,a)
    # if we print alphabet[0] it will print only index & alphabet[1] only print element
    print(alphabet[0], alphabet[1])

# the cleaner way
for index, alphabet in enumerate(alphabets):
    print(index, alphabet)

# Adding  items in lists

# append() add new new item at the end of list
letters.append('x')

# insert item add new element at the specified index you must pass index or it will throw exception
letters.insert(0, 'y')
print(letters)

# Removing items in lists

# pop method is used to remove element at specified index
# if we don't pass index number it will remove last element of list
letters.pop(0)

# remove() is used when you know the element & don't know the index
letters.remove('b')

# del is also used to remove elements from lists
# the main difference is we can remove multiple items from list
del letters[0:3]

# clear() make the list empty
letters.clear()
print(letters)

# finding items in lists
list_1 = ['a', 'b', 'c']
# index() is used to return the index of the given element
# print(list_1.index('a'))

# if we pass 'd' in the above it will throw error to prevent this we can use the following methods

# this will run in 'd' exists in list_1
if 'd' in list_1:
    print(list_1.index('d'))

# the count() is also helpful it returns the total occurences of element in list
# if you don't pass any argument in count() it will throw exception

# print(list_1.count('d'))

# Sorting lists
ages = [1, 45, 26, 34, 23]
ages.sort()
print(ages)

# if you sort and print at same time it will return None
# print(ages.sort())

# to reverse sort
ages.sort(reverse=True)
print(ages)

# the sorted() makes a copy of orignal list and sort it without modifying originnal list
ids = [1, 45, 78, 90, 2, 0]
print(sorted(ids))
print(ids)

# to sort in reverse order
print(sorted(ids, reverse=True))

# if you want to sort a list of tuple
# then it will not be sorted with sort() or sorted()
# you have to make a function
items = [('Porduct1', 19), ('Product2', 12), ('Products3', 31)]


def sort_items(item):
    """retunrs index"""
    return item[1]


items.sort(key=sort_items, )
print(items)

# lambda functions are the anonymus functions.
# We can use lamba functions to solve the above problem effectively
# this is the format of lambda  items.sort(key=lambda parameter: expression)
items.sort(key=lambda item: item[1])
print(items)

# if you want to take the prices in items array and covert it
# into list so for this pupose we can use map()
# The item functions return an object
x = map(lambda item: item[1], items)

# if we print x the output will be like this <map object at 0x0000024158F83D60>
print(x)

# so we have to iterate over it
for i in x:
    print(i)

# we can covert directly into list
x = list(map(lambda item: item[1], items))

print(type(x))

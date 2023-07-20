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

# if we want to print index of each element in array we can use built-in function called enumerate
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

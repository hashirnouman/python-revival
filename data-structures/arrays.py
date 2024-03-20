""" "Arrays"""
# Python also provides arrays
# Arrays are more perfromant that lists
# Only use arrays when dealing with large series or numbers & encouter performance issues
# Arrays have similar methods like lists

from array import array

# the first argument is typecode. Typecode shows the data type of array elements
numbers = array("i", [1, 2, 4, 5, 6])
print(numbers)

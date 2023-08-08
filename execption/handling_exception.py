""" Exception handling"""
try:
    age = int(input('Enter age  '))
    print(age)
# valud error is the type of error that program will throw when we enter wrong input
# we can print the actual error message and it's type
# the limitation of this code is it is handling ValueError exception
except ValueError as err:
    print('Enter number not string')
    print(err)
    print(type(err))
# Else block will run when there are no execption caught in program
else:
    print('No error')
print('hellow world')
try:
    age = int(input('Enter age  '))
    print(age)
# valud error is the type of error that program will throw when we enter wrong input
# we can print the actual error message and it's type
# the limitation of this code is it is handling ValueError exception
except ValueError as err:
    print('Enter number not string')
    print(err)
    print(type(err))
# Else block will run when there are no execption caught in program
else:
    print('No error')
print('hellow world')

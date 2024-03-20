"""Exception handling"""

# timeit package it used to calculate excecution time of piece of code
from timeit import timeit
# try:
#     age = int(input('Enter age  '))
#     print(age)
# # valud error is the type of error that program will throw when we enter wrong input
# # we can print the actual error message and it's type
# # the limitation of this code is it is handling ValueError exception
# except ValueError as err:
#     print('Enter number not string')
#     print(err)
#     print(type(err))
# # Else block will run when there are no execption caught in program
# else:
#     print('No error')
# print('hellow world')

# try:
#     age = int(input('Enter age '))
#     xFactor = 10/age
# # valud error is the type of error that program will throw when we enter wrong input
# # we can print the actual error message and it's type
# # the limitation of this code is it is handling ValueError exception
# except (ValueError, ZeroDivisionError) as err:
#     print('Enter valid age')
#     print(err)
#     print(type(err))

# # Else block will run when there are no execption caught in program
# else:
#     print('No error')
# print('hellow world')

# finally clause will always excuted


# try:
#     file = open('app.py', encoding="utf-8")
#     age = int(input('Enter age '))
#     xFactor = 10 / age
# except (ValueError, ZeroDivisionError) as err:
#     print('Enter valid age')
#     print(err)
#     print(type(err))
# else:
#     print('No error')
# finally:
#     file.close()  # Ensure file is always closed, even if an exception occurs

# finally is use to release external reousrces like files network connection db connection
try:
    with open("app.py", encoding="utf-8") as file:
        print("file opene")
    age = int(input("Enter age "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError) as err:
    print("Enter valid age")
    print(err)
    print(type(err))
else:
    print("No error")
file.close()

# raising an execption (not advised) because it is costly

CODE1 = """
def calculate_x_factor(total_age):
    if total_age <= 0:
        raise ValueError('Age cannot be 0 or less')
    else:
        print(10/total_age)


# when you raise exception in a function
# you've to call it with try catch else it will throw error

try:
    calculate_x_factor(0)
except ValueError as error:
    pass
"""
# this approach is faster
CODE2 = """
def calculate_x_factor(total_age):
    if total_age <= 0:
        return None
    else:
        print(10/total_age)


# when you raise exception in a function
# you've to call it with try catch else it will throw error


result = calculate_x_factor(0)
if result == None:
    pass
"""
# number is number of execution. This should be greater to see the time difference
print(timeit(CODE1, number=10000))
print(timeit(CODE2, number=10000))
# cost of raising an exception

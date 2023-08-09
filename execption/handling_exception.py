""" Exception handling"""
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
    with open('app.py', encoding="utf-8") as file:
        print('file opene')
    age = int(input('Enter age '))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError) as err:
    print('Enter valid age')
    print(err)
    print(type(err))
else:
    print('No error')

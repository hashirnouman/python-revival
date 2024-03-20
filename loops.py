"""loops"""

# it will run from 1 till before 4
SUCCESSFUL = True
# for number in range(1,4):
#     print("helo", number , (number ) * "*")


# for number in range(3):
#     print("helo")
#     if SUCCESSFUL:
#         print('Success')
#         break

# for else statement
for number in range(3):
    print("sending email")
    if SUCCESSFUL:
        print("Success")
        break
else:
    print("atempted three times but fail")

# while loop
COMMAND = ""

# while COMMAND.lower() != "quit":
#     COMMAND = input(">")
#     print("ECHO", COMMAND)


while True:
    COMMAND = input(">")
    print("ECHO", COMMAND)
    if COMMAND.lower() == "quit":
        break

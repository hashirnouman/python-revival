"""loops"""
# it will run from 1 till before 4
successful = True
# for number in range(1,4):
#     print("helo", number , (number ) * "*")


# for number in range(3):
#     print("helo")
#     if successful:
#         print('Success')
#         break

# for else statement
for number in range(3):
    print("sending email")
    if successful:
        print("Success")
        break
else:
    print("atempted three times but fail")

# while loop
command = ""

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

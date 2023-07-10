"""exercise 1"""
COUNT = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        COUNT += 1
print(f"we have COUNTer {COUNT} number")

import random
import string

print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))
print(string.ascii_letters)
names = ["Hashir", "usman", "asad", "muqaddam", "hakim"]
random.shuffle(names)
print(names)

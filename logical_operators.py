""" logical operators"""

HIGH_INCOME = True
GOOD_CREDEIT = False
STUDENT = False

if HIGH_INCOME and GOOD_CREDEIT:
    print("elligilble")
else:
    print("Not elligilbe")

if HIGH_INCOME or GOOD_CREDEIT:
    print("elligilble")
else:
    print("Not elligilbe")

if (HIGH_INCOME or GOOD_CREDEIT) and not STUDENT:
    print("elligilble")
else:
    print("Not elligilbe")

# chaining comparisong operator

AGE = 18

if AGE >= 18 and AGE < 60:
    print("OK")

#this is same as above

if 18 <= AGE < 60:
    print("OK")


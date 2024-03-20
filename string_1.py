"""stinrg"""

FIRSTNAME = "   Hashir"
LASTNAME = "nouman  "
FULLNAME = f" {FIRSTNAME} {LASTNAME}"
print(FULLNAME.strip())
print(FULLNAME.rstrip())  # remove white space from end
print(FULLNAME.lstrip())  # remove white space from start
print(FULLNAME.upper())
print(FULLNAME.lower())
print(FULLNAME.title())  # Capitalize first letter of every word
print(FULLNAME.find("ir"))  # returns index of the specified string
print(FULLNAME.replace("ir"))
print("nou" in FULLNAME)
print("swfit" not in FULLNAME)  # returns true if swit doesn't exits in FULLNAME

"""Helllo world prgram"""

import requests

print("hello")
print("*" * 10)
X = 1

x = requests.get("https://w3schools.com/python/demopage.htm")

print(x.text)

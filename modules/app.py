"""main module"""
# we can import modules in these two wal
# importing specific fucntion
# from sales import calculate_tax, calculate_mothly_sales

# import module as an object
# import sys
import ecom.shopping.sales as sales

print(dir(sales))
# sales.calculate_tax()
print(sales.__name__)
print(sales.__package__)

print(__name__)
# * imports are not recommended
# because it will import all the functions it can cause to override it.

# print(sys.path)

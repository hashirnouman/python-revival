""" main module"""
# we can import modules in these two wal
# importing specific fucntion
from sales import calculate_tax, calculate_mothly_sales

# import module as an object
import sales

sales.calculate_tax()

# * imports are not recommended
# because it will import all the functions it can cause to override it.

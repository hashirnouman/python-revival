"""command line arguments"""
import sys
if(len(sys.argv)==1):
    print("Password agument required")
else :
    password = sys.argv[1]
    print('Passowrd', password)
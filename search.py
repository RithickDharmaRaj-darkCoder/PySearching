# calling of list...
from srch_lst import *

aval_srch = ['Linear','Binary']
print("Available Searching Methods : ",aval_srch)
flst = input("Enter the search name : ").upper()

if flst == 'LINEAR':
    linear()
elif flst == 'BINARY':
    binary()
else:
    print("Invalid Answer!")


#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")
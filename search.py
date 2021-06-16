# calling of list...
from srch_lst import *
aval_srch = ['Linear Search','Binary Search']
print("Available Searching...")
count = 1
for i in aval_srch:
    print(f'    {count}. {i},')
    count += 1

def searching():
    search_iput = input("Enter the search name : ").upper()

    if search_iput == 'LINEAR' or search_iput == 'LINEAR SEARCH' or search_iput == '1':
        linear()
    elif search_iput == 'BINARY' or search_iput == 'BINARY SEARCH' or search_iput == '2':
        binary()
    else:
        print("Invalid Answer!")
        searching()

searching()

#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")
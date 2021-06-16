# Calling of list...

def linear():
    print('---------- LINEAR SEARCH ----------')
    lsize = int(input('How many numbers want to insert : '))
    lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
    print(f'Your List : {lst}')
    fnum = int(input("Enter the element to find : "))

    for i in range(len(lst)):
        if lst[i] == fnum:
            print(f"Element fount at position {i + 1}.")
            continue
    else:
        if fnum not in lst:
            print("Element not in the list!")

def binary():
    print('---------- BINARY SEARCH ----------')
    lsize = int(input('How many numbers want to insert : '))
    lst = [int(input(f'Add Number {i + 1} : ')) for i in range(lsize)]
    print(f'Your List : {lst}')
    fnum = int(input("\nEnter the numbers to find : "))
    lst.sort()
    l = 0
    u = len(lst) - 1
    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == fnum:
            print(f"{fnum} is found at position {mid + 1}.")
            break
        elif lst[mid] < fnum:
            l = mid + 1
        elif lst[mid] > fnum:
            u = mid - 1
    else:
        print("Number not in the list!")
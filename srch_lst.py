# Calling of list...

def linear():
    lst = []
    lsize = int(input("\nEnter how many elements to be insert : "))
    for i in range(lsize):
        elst = input("Enter the elements to add it in list : ")
        lst.append(elst)
    print(lst)
    fnum = input("\nEnter the element to find : ")

    for i in range(len(lst)):
        if lst[i] == fnum:
            print(f"Element fount at position {i+1}.")
            break
    else:
        print("Element not in the list!")

def binary():
    lst = []
    lsize = int(input("\nEnter how many numbers to be insert : "))
    for i in range(lsize):
        elst = int(input("Enter the numbers to add it in list : "))
        lst.append(elst)
    lst.sort()
    print(lst)
    fnum = int(input("\nEnter the numbers to find : "))

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
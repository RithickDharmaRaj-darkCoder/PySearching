

lst = []
lsize = int(input("Enter how many elements to be insert : "))
print()
for i in range(lsize):
    elst = input("Enter the elements to add it in list : ")
    lst.append(elst)
print(lst)
fnum = input("\nEnter the element to find : ")

for i in range(len(lst)):
    if lst[i] == fnum:
        print(f"Element fount at {i+1}th position in list.")
        break
else:
    print("Element not in the list!")


#Personal Greetings...
print("\nThank You!\n          -darkCoder \U0001F43E")
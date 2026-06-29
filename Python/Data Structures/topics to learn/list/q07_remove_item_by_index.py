lst=[10,20,30,40,50]

index=int(input("Enter index: "))

if 0 <= index < len(lst):
    lst.pop(index)
    print("Updated List:", lst)
else:
    print("Invalid Index")

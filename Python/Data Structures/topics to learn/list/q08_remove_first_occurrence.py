lst=[10,20,30,20,40,50]

item=int(input("Enter element to remove: "))

if item in lst:
    lst.remove(item)
    print("Updated List:", lst)
else:
    print("Element not found")

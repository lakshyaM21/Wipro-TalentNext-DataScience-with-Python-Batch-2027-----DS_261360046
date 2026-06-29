t=(10,20,30,40,50)

item=int(input("Enter element: "))

if item in t:
    print("Index =", t.index(item))
else:
    print("Element not found")

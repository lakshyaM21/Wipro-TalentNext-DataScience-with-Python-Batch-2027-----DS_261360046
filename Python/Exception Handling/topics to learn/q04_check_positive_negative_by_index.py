lst = [10, -5, 20, -8, 30, -12, 40, -1, 50, -25]

try:
    index = int(input("Enter index (0-9): "))

    if lst[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Error: Invalid index.")

except ValueError:
    print("Error: Please enter a valid integer.")

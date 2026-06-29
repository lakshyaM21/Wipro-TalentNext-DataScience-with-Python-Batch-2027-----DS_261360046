filename = input("Enter file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

print(lines)

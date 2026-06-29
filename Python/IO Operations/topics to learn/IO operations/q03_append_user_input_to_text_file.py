filename = input("Enter file name: ")
text = input("Enter text to append: ")

with open(filename, "a") as file:
    file.write(text + "\n")

print("Data appended successfully.")

try:
    filename = input("Enter file name: ")

    with open(filename, "r") as f:
        data = f.read()

    print(data.title())

except FileNotFoundError:
    print("Error: File not found.")

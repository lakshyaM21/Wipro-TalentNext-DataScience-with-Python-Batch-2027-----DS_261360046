filename = input("Enter file name: ")
n = int(input("Enter number of lines: "))

with open(filename, "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end="")

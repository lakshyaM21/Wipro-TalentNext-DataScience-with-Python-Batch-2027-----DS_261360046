filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, "r") as file:
    data = file.read().lower()

count = data.split().count(word.lower())

print("Frequency =", count)

s = input("Enter a string: ")

if s.startswith("x"):
    s = s[1:]

if s.endswith("x"):
    s = s[:-1]

print(s)

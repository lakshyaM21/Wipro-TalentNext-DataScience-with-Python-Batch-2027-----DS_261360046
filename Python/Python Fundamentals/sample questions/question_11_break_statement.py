print("No. Statements written after break inside the same block are never executed.")

for i in range(5):
    if i == 2:
        break
        print("This will never run")

try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not Prime")
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime")
        else:
            print("Not Prime")

except ValueError:
    print("Error: Please enter a valid number.")

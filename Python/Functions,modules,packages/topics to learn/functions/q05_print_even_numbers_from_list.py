def even_numbers(lst):
    for i in lst:
        if i % 2 == 0:
            print(i, end=" ")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers(numbers)

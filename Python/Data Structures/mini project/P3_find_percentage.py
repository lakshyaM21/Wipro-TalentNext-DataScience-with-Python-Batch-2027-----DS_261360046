students_and_their_grades_storage = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

who_to_search_for = input("Enter a name: ")

total_added_up = sum(students_and_their_grades_storage[who_to_search_for])
how_many_subjects = len(students_and_their_grades_storage[who_to_search_for])

the_final_average = int(total_added_up / how_many_subjects)

print(f"Average percentage mark: {the_final_average}")

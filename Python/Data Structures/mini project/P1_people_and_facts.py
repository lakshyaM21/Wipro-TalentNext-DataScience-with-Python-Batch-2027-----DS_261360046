the_people_facts_directory = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

for person_name, fact_about_them in the_people_facts_directory.items():
    print(f"{person_name}: {fact_about_them}")

print()

the_people_facts_directory["Jeff"] = "Is afraid of heights."
the_people_facts_directory["Jill"] = "Can hula dance."

for who, what in the_people_facts_directory.items():
    print(f"{who}: {what}")

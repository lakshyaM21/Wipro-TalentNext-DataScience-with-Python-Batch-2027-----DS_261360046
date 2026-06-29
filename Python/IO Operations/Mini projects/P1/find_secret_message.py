file_name = input("Enter the text file name: ")

with open(file_name, 'r') as file:
    lines = file.readlines()

number_of_lines = len(lines)

if number_of_lines > 12:
    if number_of_lines == 24:
        meeting_time = "12 AM"
    else:
        meeting_time = f"{number_of_lines - 12} PM"
elif number_of_lines == 12:
    meeting_time = "12 PM"
else:
    meeting_time = f"{number_of_lines} AM"

word_occurrences = {}

for line in lines:
    cleaned_string = ""
    for character in line:
        if character.isalnum() or character.isspace():
            cleaned_string += character
        else:
            cleaned_string += " "
            
    words = cleaned_string.split()
    
    for word in words:
        word_lower = word.lower()
        if word_lower in word_occurrences:
            word_occurrences[word_lower] += 1
        else:
            word_occurrences[word_lower] = 1

most_frequent_word = ""
highest_count = 0

for word, count in word_occurrences.items():
    if count > highest_count:
        highest_count = count
        most_frequent_word = word

meeting_place = most_frequent_word.capitalize()

print(f"\nMeeting time: {meeting_time}")
print(f"Meeting place: {meeting_place} Street")

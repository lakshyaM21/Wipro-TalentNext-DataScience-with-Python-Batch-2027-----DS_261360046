def ispalindrome(name):
    flipped_version = name[::-1]
    if name == flipped_version:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    the_magic_vowels = "aeiouAEIOU"
    the_final_tally = sum(1 for single_character in name if single_character in the_magic_vowels)
    print(f"No of vowels: {the_final_tally}")

def frequency_of_letters(name):
    storage_for_counts = {}
    for distinct_letter in name:
        storage_for_counts[distinct_letter] = storage_for_counts.get(distinct_letter, 0) + 1
        
    compiled_results = []
    for the_key, the_value in storage_for_counts.items():
        compiled_results.append(f"{the_key}-{the_value}")
        
    print("Frequency of letters:", ", ".join(compiled_results))

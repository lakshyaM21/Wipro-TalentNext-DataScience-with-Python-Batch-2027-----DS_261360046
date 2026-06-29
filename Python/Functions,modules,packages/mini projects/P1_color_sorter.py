def make_the_colors_organized(the_jumbled_text):
    the_broken_pieces = the_jumbled_text.split('-')
    the_broken_pieces.sort()
    the_glued_back_text = "-".join(the_broken_pieces)
    return the_glued_back_text

what_the_user_typed = input("Sample input: ")
the_end_result = make_the_colors_organized(what_the_user_typed)
print("Sample output:", the_end_result)

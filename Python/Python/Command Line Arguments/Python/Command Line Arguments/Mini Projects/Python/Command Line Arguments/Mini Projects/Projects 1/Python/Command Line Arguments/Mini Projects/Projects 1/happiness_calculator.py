import sys

def calculate_the_vibes(things_that_make_me_smile, things_that_make_me_frown, the_bag_of_stuff_i_found):
    happy_things = set(things_that_make_me_smile.split('-'))
    sad_things = set(things_that_make_me_frown.split('-'))
    
    the_current_vibe_check = sum(
        (one_single_thing in happy_things) - (one_single_thing in sad_things) 
        for one_single_thing in the_bag_of_stuff_i_found.split('-')
    )
    
    return the_current_vibe_check

if len(sys.argv) > 3:
    the_good_numbers = sys.argv[1]
    the_bad_numbers = sys.argv[2]
    the_numbers_to_check = sys.argv[3]
    
    final_score_of_my_day = calculate_the_vibes(the_good_numbers, the_bad_numbers, the_numbers_to_check)
    print(final_score_of_my_day)

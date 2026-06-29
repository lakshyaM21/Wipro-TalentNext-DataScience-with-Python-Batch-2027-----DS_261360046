import sys

if len(sys.argv) == 3:
    the_first_number = int(sys.argv[1])
    the_second_number = int(sys.argv[2])
    
    total_added_up = the_first_number + the_second_number
    print("The sum of the two numbers is:", total_added_up)
else:
    print("Please provide exactly two numbers when running this script.")

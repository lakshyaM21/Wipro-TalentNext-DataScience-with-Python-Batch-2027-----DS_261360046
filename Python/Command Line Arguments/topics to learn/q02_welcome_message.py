import sys

if len(sys.argv) > 1:
    the_script_name_itself = sys.argv[0]
    the_warm_welcome_message = " ".join(sys.argv[1:])
    
    print(f"File Name: {the_script_name_itself}")
    print(f"Message: {the_warm_welcome_message}")
else:
    print("Please provide a welcome message when running this script.")

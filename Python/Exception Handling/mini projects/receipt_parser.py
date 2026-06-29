def process_my_shopping_cart(what_is_the_file_called):
    if not what_is_the_file_called.endswith(".txt"):
        what_is_the_file_called += ".txt"
        
    how_many_things_i_bought = 0
    how_many_things_were_free = 0
    how_much_it_cost_me = 0
    the_discount_i_got = 0
    
    try:
        with open(what_is_the_file_called, 'r') as the_shopping_receipt:
            all_the_lines = the_shopping_receipt.readlines()
            
            for one_single_line in all_the_lines:
                the_cleaned_up_line = one_single_line.strip()
                
                if not the_cleaned_up_line:
                    continue
                    
                the_parts_of_the_line = the_cleaned_up_line.split()
                the_name_of_the_thing = the_parts_of_the_line[0]
                the_price_of_the_thing = the_parts_of_the_line[-1]
                
                if the_name_of_the_thing.lower() == "discount":
                    try:
                        the_discount_i_got = int(the_price_of_the_thing)
                    except ValueError:
                        the_discount_i_got = 0
                    continue
                
                try:
                    actual_money_value = int(the_price_of_the_thing)
                    how_much_it_cost_me += actual_money_value
                    how_many_things_i_bought += 1
                except ValueError:
                    if the_price_of_the_thing.lower() == "free":
                        how_many_things_were_free += 1
                        how_many_things_i_bought += 1
                        
    except FileNotFoundError:
        print("I couldn't find that file! Did you misspell it?")
        return
    except Exception as weird_error:
        print(f"Something really strange happened: {weird_error}")
        return

    the_money_i_actually_paid = how_much_it_cost_me - the_discount_i_got
    
    print(f"No of items purchased: {how_many_things_i_bought}")
    print(f"No of free items: {how_many_things_were_free}")
    print(f"Amount to pay: {how_much_it_cost_me}")
    print(f"Discount given: {the_discount_i_got}")
    print(f"Final amount paid: {the_money_i_actually_paid}")


the_file_the_user_wants = input("Enter the file name: ")
process_my_shopping_cart(the_file_the_user_wants)

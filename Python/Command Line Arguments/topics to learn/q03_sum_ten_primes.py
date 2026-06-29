import sys

def check_if_it_is_prime(the_number_to_test):
    if the_number_to_test <= 1:
        return False
    for potential_divisor in range(2, the_number_to_test):
        if the_number_to_test % potential_divisor == 0:
            return False
    return True

if len(sys.argv) == 11:
    running_total_of_primes = 0
    
    for string_number in sys.argv[1:]:
        actual_number = int(string_number)
        if check_if_it_is_prime(actual_number):
            running_total_of_primes += actual_number
            
    print("The final sum of all the prime numbers you gave me is:", running_total_of_primes)
else:
    print("You need to provide exactly 10 numbers as arguments!")

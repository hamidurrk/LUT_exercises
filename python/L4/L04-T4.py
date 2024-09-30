# L04-T4: Extensions of repeat structures
#
# Submitted by: Md Hamidur Rahman Khan
#

lower_limit = int(input("Enter the lower limit of the range:\n"))
upper_limit = int(input("Enter the upper limit of the range:\n"))
FOUND_VALUE = False         # Flag to check if any value was found

# Fuction to check if a number is divisible by 5
def is_divisible_by_5(num):
    if(num % 5 == 0):
        return True
    else:
        return False

# Fuction to check if a number is divisible by 7
def is_divisible_by_7(num):
    if(num % 7 == 0):
        return True
    else:
        return False

# Search loop using for
for x in range(lower_limit, upper_limit + 1):
    if not is_divisible_by_5(x):
        print(f"{x} is NOT divisible by 5, rejecting.")
        continue
    elif not is_divisible_by_7(x):
        print(f"{x} is NOT divisible by 7, rejecting.")
        continue
    else:
        print(f"The number {x} is divisible by 5 and 7.\nStopping the search.")
        FOUND_VALUE = True
        break

# If no value was found in the range, print a message
if not FOUND_VALUE:
    print("No suitable value was found in the range.")
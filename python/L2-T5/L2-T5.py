# L02-T5: Average calculation, print formatting, integer and rotation
#
# Submitted by: Md Hamidur Rahman Khan
#

print("This program calculates the average of the 3 numbers you enter.\nThe numbers can be int's or float's.")

first_number = float(input("Enter the first number:\n"))

second_number = float(input("Enter the second number:\n"))

third_number = float(input("Enter the third number:\n"))


sum = first_number + second_number + third_number

# Checking if sum is an integer so that it doesn't print a float in the output (eg. 3.0)
if(float.is_integer(sum)):                      
    sum = int(sum)

avg = sum / 3
avg_rounded_to_3_decimal_places = round(avg, 3) # Rounding to 3 decimal places
avg_rounded_to_closest_int = round(avg) # Rounding to the closest integer
avg_wo_decimal = int(avg)  # Just removing the decimal part

# Printing the outputs
print(f"Sum of the numbers: {sum}")
print(f"Average of the numbers (rounded to 3 decimal places): {avg_rounded_to_3_decimal_places}")
print(f"Average of the numbers (rounded to the closest integer): {avg_rounded_to_closest_int}")
print(f"Average of the numbers as an integer without the decimal part: {avg_wo_decimal}")
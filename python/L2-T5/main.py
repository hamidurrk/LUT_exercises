# L02-T5: Average calculation, print formatting, integer and rotation
#
# Submitted by: Md Hamidur Rahman Khan
#

print("This program calculates the average of the 3 numbers you enter.\nThe numbers can be int's or float's.")

first_number = float(input("Enter the first number: "))

second_number = float(input("Enter the second number: "))

third_number = float(input("Enter the third number: "))


sum = first_number + second_number + third_number
if(float.is_integer(sum)):
    sum = int(sum)
avg = sum / 3
avg_rounded_to_3_decimal_places = round(avg, 3)
avg_rounded_to_closest_int = round(avg)
avg_wo_decimal = int(avg)

print(f"\nSum of the numbers: {sum}")
print(f"Average of the numbers (rounded to 3 decimal places): {avg_rounded_to_3_decimal_places}")
print(f"Average of the numbers (rounded to the closest integer): {avg_rounded_to_closest_int}")
print(f"Average of the numbers as an integer without the decimal part: {avg_wo_decimal}")

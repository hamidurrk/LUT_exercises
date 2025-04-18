print("This program calculates the average of the 3 numbers you enter.\nThe numbers can be int's or float's.")

first_number = float(input("Enter the first number:\n"))
second_number = float(input("Enter the second number:\n"))
third_number = float(input("Enter the third number:\n"))

sum = first_number + second_number + third_number

average = sum / 3
average_rounded_to_three_decimal_places = round(average, 3) 
average_rounded_to_closest_int = round(average) 
average_without_decimal = int(average)  

print(f"Sum of the numbers: {sum}")
print(f"Average of the numbers (rounded to 3 decimal places): {average_rounded_to_three_decimal_places}")
print(f"Average of the numbers (rounded to the closest integer): {average_rounded_to_closest_int}")
print(f"Average of the numbers as an integer without the decimal part: {average_without_decimal}")
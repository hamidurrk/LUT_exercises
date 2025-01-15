print("This program calculates the average of the 3 numbers you enter.")

nums = []

nums.append(float(input("Enter the first number:\n")))
nums.append(float(input("Enter the second number:\n")))
nums.append(float(input("Enter the third number:\n")))

print(f"Sum of the numbers: {sum(nums)}")

print(f"Average of the numbers (rounded to 3 decimal places): {round(sum(nums)/len(nums), 3)}")
print(f"Average of the numbers (rounded to the closest integer): {round(sum(nums)/len(nums))}")
print(f"Average of the numbers as an integer without the decimal part: {round(sum(nums)//len(nums))}")

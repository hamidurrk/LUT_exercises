# L02-T4: Integer, fixed value, calculation and print formatting
#
# Submitted by: Md Hamidur Rahman Khan
#

num = int(input("Enter a positive integer:\n"))
print(f"Number {num} multiplied by itself is {num ** 2}")

PII = 3.14
radius = int(input("Give the radius of a circle as an integer:\n"))
circumference = 2 * PII * radius
area = PII * (radius ** 2)
print(f"The radius of the circle is {radius}, 
      the circumference is {circumference:.2f} 
      and the area is {area:.2f}.")

side1 = int(input("Enter the length of one side of the rectangle as an integer:\n"))
side2 = int(input("Enter the length of another side of the rectangle as an integer:\n"))
perimeter = 2 * (side1 + side2)
area = side1 * side2
print(f"The sides of the rectangle are {side1} and {side2}; 
      perimeter is {perimeter}; 
      and the area is {area}.")


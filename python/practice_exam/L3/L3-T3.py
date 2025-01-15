num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

print("The calculator can perform the following operations:")
print("1) Add\n2) Subtract\n3) Multiply\n4) Divide")

print(f"The numbers you entered are {num1} and {num2}")

option = int(input("Select the operation (1-4):\n"))

if option == 1:
    print(f"Selection 1: {num1} + {num2} = {num1 + num2}")
elif option == 2:
    print(f"Selection 2: {num1} - {num2} = {num1 - num2}")
elif option == 3:
    print(f"Selection 3: {num1} * {num2} = {num1 * num2}")
elif option == 4:
    if num2 == 0:
        print("Error: Zero cannot be used as a divisor.")
    else:
        print("Selection 4: {num1} / {num2} = {num1 / num2}")
else:
    print("The operation was not recognized.")

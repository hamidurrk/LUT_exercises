num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

# Dictionary of operations
operations = {
    "1": "Enter Numbers",
    "2": "Sum",
    "3": "Subtract",
    "4": "Multiplication",
    "5": "Division",
    "6": "Power of",
    "0": "Stop"
}

# Ask the user to select an operation, print the operations from the dictionary
print("This calculator can perform the following functions:")
for key, value in operations.items():
    print(f"{key}) {value}")

print(f"The numbers you entered are {num1} and {num2}")

option = str(input("Select the operation (1-4):\n"))

def template(option, num1, num2, sign, result):
    return print(f"Selection {option}: {num1} {sign} {num2} = {result}")

if (option == "1"):
    template(option=option, num1=num1, num2=num2, sign="+", result=num1+num2)
elif (option == "2"):
    template(option=option, num1=num1, num2=num2, sign="-", result=num1-num2)
elif (option == "3"):
    template(option=option, num1=num1, num2=num2, sign="*", result=num1*num2)
elif (option == "4"):
    if (num2 == 0):
         print("Zero cannot be used as a divisor.")
    else:
        template(option=option, num1=num1, num2=num2, sign="/", result=round(num1/num2, 2))
else:
    print("The operation was not recognized.")
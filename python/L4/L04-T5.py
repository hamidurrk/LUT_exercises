# L04-T5: Menu-based program, continuing from exercise L03-T3 
#
# Submitted by: Md Hamidur Rahman Khan
#

# Declaring variables without assigning values
num1: int
num2: int

# Defining a template to print the results easily
def template(option, num1, num2, sign, result):
    return print(f"{option} {num1} {sign} {num2} = {result}")

# Dictionary of operations
operations = {
    "1": "Enter numbers",
    "2": "Sum",
    "3": "Subtract",
    "4": "Multiplication",
    "5": "Division",
    "6": "Power of",
    "0": "Stop"
}

while True:
    try:
        # Ask the user to select an operation, print the operations from the dictionary
        print("This calculator can perform the following functions:")
        for key, value in operations.items():
            print(f"{key}) {value}")

        option = str(input("Select function (0-6):\n"))

        if (option == "0"):
            print("Stopping\nBye")
            break
        elif (option == "1"):
            num1 = int(input("Enter the first number:\n"))
            num2 = int(input("Enter the second number:\n"))
            print(f"You entered numbers {num1} and {num2}")
        elif (option == "2"):       # Sum
            template(option=operations[option], num1=num1, num2=num2, sign="+", result=num1+num2)
        elif (option == "3"):       # Subtract
            template(option="Subtraction", num1=num1, num2=num2, sign="-", result=num1-num2)
        elif (option == "4"):       # Multiplication
            template(option=operations[option], num1=num1, num2=num2, sign="*", result=num1*num2)
        elif (option == "5"):       # Division
            if (num2 == 0):
                print("Cannot divide by zero.")
            else:
                template(option=operations[option], num1=num1, num2=num2, sign="/", result=round(num1/num2, 2))
        elif (option == "6"):       # Power of
            # template(option=operations[option], num1=num1, num2=f"\b{num2}", sign="\b**", result=num1**num2)
            print(f"Power of {num1}**{num2} = {num1**num2}")
        else:
            print("Unknown selection, try again.")
    except NameError:
        print("You haven't entered any numbers yet. Select function 1 to enter numbers.")
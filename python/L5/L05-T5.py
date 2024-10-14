# L05-T5: Menu-based program / Calculator. Continuing from L04-T5
#
# Submitted by: Md Hamidur Rahman Khan
#

# Declaring variables without assigning values
num1: int
num2: int

# Dictionary of operations
operations = {
    "1": "Enter numbers",
    "2": "Sum",
    "3": "Subtract",
    "4": "Multiplication",
    "5": "Division",
    "0": "Stop"
}

# Defining a template to print the results easily
def template(option, num1, num2, sign, result):
    return print(f"{option} {num1} {sign} {num2} = {result}")

def menu():
    print("This calculator can perform the following functions:")
    for key, value in operations.items():
        print(f"{key}) {value}")
    option = str(input("Select function (0-5):\n"))
    return option

def enter_integer(text : str) -> int:
    return int(input(text))

def sum(value1: int, value2: int) -> str:
    print(f"Sum {value1} + {value2} = {value1+value2}")
 
def subtract(value1: int, value2: int) -> str:
    print(f"Subtract {value1} - {value2} = {value1-value2}")

def multiplication(value1: int, value2: int) -> str:
    return str(value1 * value2)

def division(value1: int, value2: int) -> str:
    if (value2 == 0):
        return"You cannot divide by zero."
    else:
        return f"{value1} {"/"} {value2} = {round(value1/value2, 2)}"

def main():
    while True:
        try:
            # Ask the user to select an operation, print the operations from the dictionary
            option = menu()

            if (option == "0"):
                print("Stopping\nBye")
                break
            elif (option == "1"):
                num1 = enter_integer("Enter the first number: \n")
                num2 = enter_integer("Enter the second number: \n")
                print(f"You inputted integers {num1} and {num2}")
            elif (option == "2"):       # Sum
                template(option=operations[option], num1=num1, num2=num2, sign="+", result=sum(num1, num2))
            elif (option == "3"):       # Subtract
                template(option=operations[option], num1=num1, num2=num2, sign="-", result=subtract(num1, num2))
            elif (option == "4"):       # Multiplication
                template(option=operations[option], num1=num1, num2=num2, sign="*", result=multiplication(num1, num2))
            elif (option == "5"):       # Division
                if (num2 == 0):
                    print(division(num1, num2))
                else:
                    print(f"{operations[option]} {division(num1, num2)}")
            else:
                print("Unknown selection, try again.")
        except NameError:
            print("You haven't entered any numbers yet. Select function 1 to enter numbers.")


if __name__ == "__main__":
    main()
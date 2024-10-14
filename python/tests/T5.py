def menu():
    print("Select one of the following operations:")
    print("1) Enter integers")
    print("2) Sum")
    print("3) Subtract")
    print("4) Multiplication")
    print("5) Division")
    print("0) Stop")
    
    return enter_integer("Select the function (0-5):\n")


def enter_integer(text):
    return int(input(text))


def sum(value1, value2):
    result = value1 + value2
    return f"Sum {value1} + {value2} = {result}"


def subtract(value1, value2):
    result = value1 - value2
    return f"Subtract {value1} - {value2} = {result}"


def multiplication(value1, value2):
    result = value1 * value2
    return f"Multiplication {value1} * {value2} = {result}"


def division(value1, value2):
    if value2 == 0:
        return "You cannot divide by zero."
    else:
        result = round(value1 / value2, 2)
        return f"Division {value1} / {value2} = {result}"


def power(value1, value2):
    result = value1 ** value2
    return f"{value1} raised to the power of {value2} = {result}"


def main():
    num1 = None
    num2 = None

    while True:
        op = menu()
        
        if op == 1:
            num1 = enter_integer("Enter first integer:\n")
            num2 = enter_integer("Enter second integer:\n")
            print(f"You inputted integers {num1} and {num2}")

        elif op in [2, 3, 4, 5]:
            if num1 is None or num2 is None:
                print("Please enter numbers first by selecting option 1.")
                continue

            if op == 2:
                print(sum(num1, num2))
            elif op == 3:
                print(subtract(num1, num2))
            elif op == 4:
                print(multiplication(num1, num2))
            elif op == 5:
                print(division(num1, num2))

        elif op == 0:
            print("Bye.")
            break

        else:
            print("Unknown choice, try again.")


main()

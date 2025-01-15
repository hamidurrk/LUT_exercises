options = {
    1 : "Enter numbers",
    2 : "Sum",
    3 : "Subtract",
    4 : "Multiplication",
    5 : "Division",
    6 : "Power of",
    0 : "Stop"
    }

def menu():
    print("This calculator can perform the following functions:")
    for option in options.keys():
        print(f"{option}) {options[option]}")
    selected = int(input("Select function (0-6):\n"))
    if selected not in options.keys():
        print("Unknown selection, try again.")
        return None
    else:
        return selected

def main():
    num1, num2 = None, None
    while True:
        s = menu()
        if s != None:
            if s == 1:
                num1 = int(input("Enter the first number:\n"))
                num2 = int(input("Enter the second number:\n"))
                print(num1, num2)
            elif s in [2, 3, 4, 5, 6]:
                if num1 != None and num2 != None:
                    if s == 2:
                        print(num1+num2)
                    elif s == 3:
                        print(num1-num2)
                    elif s == 4:
                        print(num1*num2)
                    elif s == 5:
                        if num2 == 0:
                            print("Cannot divide by zero!")
                        else:
                            print(num1/num2)
                    elif s == 6:
                        print(num1**num2)
                else:
                    print("Enter values first.")
            elif s == 0:
                print("Bye!")
                break

main()

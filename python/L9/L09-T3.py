# L09-T3: Handling exceptions with user input
#
# Submitted by: Md Hamidur Rahman Khan
#

import math

operations = {
    "1": "Test for ValueError",
    "2": "Test for IndexError",
    "3": "Test for ZeroDivisionError",
    "4": "Test for TypeError",
    "0": "Stop"
}

def valueError():
    try:
        num = int(input("Give a non-negative integer: \n"))
        print(f"Square root of {num} is {round(math.sqrt(num), 2)}.")
    except ValueError:
        print("ValueError happened. Non-negative number expected for square root.")

def indexError():
    try:
        int_list = [11, 22, 33, 44, 55]
        index = int(input("Input index 0-4: \n"))
        print(f"List value is {int_list[index]} at index {index}.")
    except IndexError:
        print(f"Got an IndexError with index {index}.")

def zeroDivisionError():
    try:
        divider = int(input("Enter divider: \n"))
        print(f"4/{divider} = {round(4/divider, 2)}.")
    except ZeroDivisionError:
        print(f"ZeroDivisionError occurred, divider {divider}.")
 
def typeError():
    try:
        num = input("Enter number:\n")
        try:
            num = int(num)
        except ValueError:
            pass
        print(f"{num}*{num} = {round(num*num, 2)}")
    except TypeError:
        print("Got TypeError. Two strings cannot be multiplied together.")       

def menu():
    print("What do you want to do:")
    for key, value in operations.items():
        print(f"{key}) {value}")
    try:
        while True:
            try:
                option_choice = int(input("Your choice:\n"))
                break
            except ValueError:
                print("ValueError happened. Enter the selection as an integer.")
        option = operations[str(option_choice)]
    except:
        option = "Invalid"
    return option
 
def main():
    while True:
        option = menu()
        match option:
            case "Test for ValueError":
                valueError()
            case "Test for IndexError":
                indexError()
            case "Test for ZeroDivisionError":
                zeroDivisionError()
            case "Test for TypeError":
                typeError()
            case "Invalid":
                print("Unknown selection, please try again.")
            case "Stop":
                print("See you again!")
                break
main()
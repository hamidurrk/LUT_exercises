# L08-T1: Using Python libraries: Math & Random
#
# Submitted by: Md Hamidur Rahman Khan
#

import math
import random

random.seed(1)

operations = {
    "1": "Calculate the area of the circle",
    "2": "Guess the number",
    "0": "Stop"
}

def menu():
    print("What do you want to do:")
    for key, value in operations.items():
        print(f"{key}) {value}")
    try:
        option = operations[input("Your choice:\n")]
    except:
        option = "Invalid"
    return option

def calc_circle_area():
    radius = int(input("Enter the radius of the circle as an integer:\n"))
    print(f"With a radius of {radius}, the area of the circle is {round(math.pi*(radius**2), 2)}.")

def guessing_game():
    target, tries = random.randint(0, 1000), 1
    print("Guess the integer drawn by the program.")
    while True:
        guess = int(input("Enter an integer between 0 and 1000:\n"))
        messages = {(False, False): "The requested number is lower.", (True, False): "The requested number is higher.", (False, True): f"Correct! You used {tries} tries to guess the correct integer."}
        result = (guess < target, guess == target)
        print(messages[result])
        tries += not result[1]
        if result[1]: break

def main():
    print("This program uses libraries to solve tasks.")
    while True:
        option = menu()
        match option:
            case "Calculate the area of the circle":
                calc_circle_area()
            case "Guess the number":
                guessing_game()
            case "Invalid":
                print("Unknown choice, please try again.")
            case "Stop":
                print("See you again!")
                break
        print("")
main()
import math, random

random.seed(1)

def calculte_area():
    r = int(input("Enter the radius of the circle as an integer:\n"))
    print(f"With a radius of {r}, the area of the circle is {math.pi * (r**2)}")

def guess_the_number():
    print("Guess the integer drawn by the program.")
    number = random.randint(0, 1000)
    count = 1
    while True:
        guess = int(input("Enter an integer between 0 to 1000:\n"))
        if guess < number:
            print("The requested number is higher.")
        elif guess > number:
            print("The requested number is lower.")
        else:
            print(f"Correct! You used {count} tries to solve the problem.")
            break
        count+= 1
        
def main():
    while True:
        print("This program uses libraries to solve tasks.")
        choice = int(input("Your choice:\n"))
        if choice == 1:
            calculate_area()
        elif choice == 2:
            guess_the_number()
        elif choice == 0:
            break
        else:
            print("Unknown selection.")
        print()
    
main()

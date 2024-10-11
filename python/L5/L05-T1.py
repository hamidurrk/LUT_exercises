# L05-T1: Three different simple versions of a function
#
# Submitted by: Md Hamidur Rahman Khan
#

# a) Print inside a function

def print_lines():
    print("This is printed inside the function")
    
# b) Input parameters and calculation

def process_number(nr : int):
    print("The input number is: ", nr)
    
    square_of_the_value = nr**2
    
    print("The number squared is: ", square_of_the_value)
    
# c) Printing the name

def print_whole_name():
    first_name = input("Enter your first name:\n")
    last_name = input("Enter your last name:\n")
    
    print(f"The full name is {first_name} {last_name}")
        
# calling the functions

print("Function 1:")
print_lines()

print("\nFunction 2:")
user_input = int(input("Enter a number:\n"))
process_number(user_input)

print("\nFunction 3:")
print_whole_name()
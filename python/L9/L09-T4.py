# L09-T4:  Handling multiple exceptions
#
# Submitted by: Md Hamidur Rahman Khan
#

global num1, num2

def exception_handler(subroutine, *args):
    try:
        subroutine(*args)
    except ValueError:
        print("You must enter valid numbers")
    except ZeroDivisionError:
        print("You cannot divide by zero")
    
def divide(num1, num2):
    num1 = float(num1)
    num2 = float(num2) 
    print(f"The result of {num1} / {num2} is {num1/num2:.8f}")
    
if __name__ == "__main__":
    num1 = input("Enter the first number:\n")
    num2 = input("Enter the second number:\n")
    
    exception_handler(divide, num1, num2)

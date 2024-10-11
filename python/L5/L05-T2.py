# L05-T2: Function with parameters, value comparison
#
# Submitted by: Md Hamidur Rahman Khan
#

def compare(num1, num2):
    x = None
    if not num1 == num2:
        if num1 > num2:
            pass 
        else:
            x = num1
            num1 = num2
            num2 = x
        print(f"{num1} is greater than {num2}")
    else:
        print("The integers are the same.")
    return num1

numbers = []
numbers.append(int(input("Enter the first integer:\n")))
numbers.append(int(input("Enter the second integer:\n")))
result = compare(numbers[0], numbers[1])

numbers = numbers[::-1] if not result == numbers[0] else numbers

num3 = int(input("Enter the integer that is subtracted from the larger:\n"))
result = result - num3
compare(result, numbers[1])
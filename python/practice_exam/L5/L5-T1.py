def print_lines():
    print("This is printed inside the function")

def process_number(nr :int):
    print(f"The input number is {nr}")
    print(f"The number squared is {nr ** 2}")

def print_whole_name():
    f_name = input("Enter your first name:\n")
    l_name = input("Enter your last name:\n")

    print(f"The full name is {f_name} {l_name}")

for i in range(1, 4):
    print(f"Function {i}:")
    if i == 1:
        print_lines()
        print()
    if i == 2:
        num = int(input("Enter a number:\n"))
        process_number(num)
        print()
    if i == 3:
        print_whole_name()

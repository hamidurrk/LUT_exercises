name = input("Enter your name:\n")
num_int = int(input("Enter an integer\n"))
num_float = float(input("Enter a float\n"))

print(f"Decimal {num_float} to power {num_int} is {round(num_float ** num_int, 2)}")
print(f"Thank you for using the program, {name}!")

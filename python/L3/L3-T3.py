num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

print("The calculator can perform the following operations:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide")
print(f"The numbers you entered are {num1} and {num2}")

option = str(input("Select the operation (1-4):\n"))

def template(option, num1, num2, sign, result):
    return print(f"Selection {option}: {num1} {sign} {num2} = {result}")

if (option == "1"):
    template(option=option, num1=num1, num2=num2, sign="+", result=num1+num2)
elif (option == "2"):
    template(option=option, num1=num1, num2=num2, sign="-", result=num1-num2)
elif (option == "3"):
    template(option=option, num1=num1, num2=num2, sign="*", result=num1*num2)
elif (option == "4"):
    if (num2 == 0):
         print("Zero cannot be used as a divisor.")
    else:
        template(option=option, num1=num1, num2=num2, sign="/", result=round(num1/num2, 2))
else:
    print("The operation was not recognized.")
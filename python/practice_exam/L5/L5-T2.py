def compare(num1, num2):
    pivot = None
    if num1 != num2:
        if num1 > num2:
            pass
        else:
            pivot, num1, num2 = num1, num2, pivot
        print(num1, "is greater than", num2)
    else:
        print("The integers are the same.")
    return num1

a = int(input("Enter the first int:\n"))
b = int(input("Enter the second int:\n"))

larger = compare(a, b)

c = int(input("Enter the integer that is subtracted from the larger:\n"))

compare(larger-c, a if larger == b else b)

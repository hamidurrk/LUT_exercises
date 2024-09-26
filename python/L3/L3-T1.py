year = int(input("Enter a year:\n"))
flag = 0

if (year % 4 == 0):
    if (year % 100 == 0 and year % 400 != 0):
        flag = 0
    flag = 1

if (flag):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
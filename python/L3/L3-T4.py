def grader(input):
    if (input >= 90.0 and input <= 100.0):
        return 5
    elif (input >= 80.0 and input < 90.0):
        return 4
    elif (input >= 70.0 and input < 80.0):
        return 3
    elif (input >= 60.0 and input < 70.0):
        return 2
    elif (input >= 50.0 and input < 60.0):
        return 1
    elif (input >= 0.0 and input < 50.0):
        return 0
    
points = float(input("Enter your number of points:\n"))

if (points <= 100 and points >= 0):
    print(f"Your grade is: {grader(points)}")
else:
    print("Invalid amount of points! Enter values within 0-100.0")
def grader(input):
    if (input >= 90 and input <= 100):
        return 5
    elif (input >= 80 and input <= 89):
        return 4
    elif (input >= 70 and input <= 79):
        return 3
    elif (input >= 60 and input <= 69):
        return 2
    elif (input >= 50 and input <= 59):
        return 1
    elif (input >= 0 and input <= 49):
        return 0
    
points = float(input("Enter your number of points:\n"))

if (points <= 100 and points >= 0):
    print(f"Your grade is: {grader(points)}")
else:
    print("Invalid amount of points! Enter values within 0-100")
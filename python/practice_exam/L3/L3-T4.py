point = float(input("Enter your number of points:\n"))
graded = False
scale = {
    90 : 5,
    80 : 4,
    70 : 3,
    60 : 2,
    50 : 1
    }

for value in scale.keys():
    if value <= point < value + 10:
        print(f"Your grade is: {scale[value]}")
        graded = True
        
if 0 <= point < 50:
    print("Your grade is: 0")
elif not graded:
    print("Your point is out of 0-100")

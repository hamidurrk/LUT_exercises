# L04-T3: Repetition structure with multiple termination conditions
#
# Submitted by: Md Hamidur Rahman Khan
#

a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))

while True:
    a *= 2
    b += 100
    if a > 1000 or b > 1000:    
        if a > 1000:
            print("a exceeded 1000")
        if b > 1000:
            print("b exceeded 1000")
        break
    print(f"a: {a} b: {b}")
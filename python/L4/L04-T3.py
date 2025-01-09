# L04-T3: Repetition structure with multiple termination conditions
#
# Submitted by: Md Hamidur Rahman Khan
#

a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))

while True:
    if a > 1000 or b > 1000:    
        if a > 1000:
            print("a exceeded 1000")
        if b > 1000:
            print("b exceeded 1000")
        break
    else:
        print(f"a: {a} b: {b}")
    
    a *= 2
    b += 100
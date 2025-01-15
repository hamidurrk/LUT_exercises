a, b = 1001, 1111

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
    

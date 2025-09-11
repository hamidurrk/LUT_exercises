def triangle(a: int, b: int, c: int):
    sides = [a, b, c]
    sides.sort()

    for side in sides:
        if side <= 0:
            return False
    
    if sides[0] + sides[1] > sides[2]:
        return True
    return False

if __name__ == "__main__":
    print(triangle(3, 5, 4))
    print(triangle(-1, 2, 3))
    print(triangle(5, 9, 14))
    print(triangle(30, 12, 29))

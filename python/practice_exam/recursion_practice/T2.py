def power(base, exp):
    if exp == 1:
        return base
    result = base * power(base, exp-1)
    return result

print(power(2, 3))


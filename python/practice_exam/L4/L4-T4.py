lower, upper = 99, 113
i = lower
found = False
while i <= upper:
    for j in [5, 7]:
        if i % j != 0:
            print(f"{i} is NOT divisible by {j}, rejecting.")
            found = False
            break
        else:
            found = True
    if found:
        print(f"The number {i} is divisible by 5 and 7.")
        break
    i += 1

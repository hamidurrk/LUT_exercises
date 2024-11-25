# L11-T1: Tuple
#
# Submitted by: Md Hamidur Rahman Khan
#

def powers(x):
    # return tuple(x**power for power in range(2, 6))
    t = [x**power for power in range(2, 6)]
    return (t[0], t[1], t[2], t[3])

def main():
    num = float(input("Enter a number:\n"))
    print(f"Powers of {num}:")
    for power, result in zip(range(2, 6), powers(num)):
        print(f"x^{power}: {round(result, 4)}")

main()
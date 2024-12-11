# L13-T2: Recursion: Sum of numbers #2
#
# Submitted by: Md Hamidur Rahman Khan
#


def sum_of_digits_recursive(n: int) -> int:
    return n if n < 10 else n % 10 + sum_of_digits_recursive(n // 10)

def main():
    number = 123456789
    print("Sum of digits using recursion: ", sum_of_digits_recursive(number))
    print("Sum of digits using list comprhension: ", sum([int(digit) for digit in str(number)]))

main()
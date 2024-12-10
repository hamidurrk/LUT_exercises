# L13-T1: Recursion: Sum of numbers #1
#
# Submitted by: Md Hamidur Rahman Khan
#


def sum_of_list_recursive(numbers: list, pointer: int = 0) -> int:
    return 0 if pointer == len(numbers) else numbers[pointer] + sum_of_list_recursive(numbers, pointer + 1)

def main():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Sum of list using recursion: ", sum_of_list_recursive(num_list))
    print("Sum of list using built-in list method: ", sum(num_list))
    
main()
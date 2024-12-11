# L13-T4: Complexity issues
#
# Submitted by: Md Hamidur Rahman Khan
#

import time

def fibonacci(n, indent="", print_tree=True):
    if n == 0:
        print(f"{indent}fibonacci(0) -> 0") if print_tree else None
        return 0
    elif n == 1:
        print(f"{indent}fibonacci(1) -> 1") if print_tree else None
        return 1
    else:
        print(f"{indent}fibonacci({n})") if print_tree else None
        left = fibonacci(n - 1, indent + "L\t", print_tree=print_tree)
        print(f"{indent}Left fibonacci({n}) left the recursion") if print_tree else None
        right = fibonacci(n - 2, indent + "R\t", print_tree=print_tree)
        print(f"{indent}Right fibonacci({n}) left the recursion") if print_tree else None
        result = left + right
        print(f"{indent}fibonacci({n}) -> {result}") if print_tree else None
        return result


def main(SHOW_TIME = False):
    n = 5
    time_start = time.time()
    f_num = fibonacci(n, print_tree=False)
    time_end = time.time()
    print(f"Fibonacci number at position {n}: {f_num}")
    print(f"Time taken for recursive approach: {time_end - time_start:.10f} seconds") if SHOW_TIME else None
    
main(SHOW_TIME = True)

# Since this naive recursive approach redundently calculates the same values multiple times, 
# and also the fact that the function calls itself twice in each iteration,
# it is not efficient for large values of n.
# The time complexity of this approach is O(2^n).

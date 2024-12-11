# L13-T5: Improved version of Fibonacci
#
# Submitted by: Md Hamidur Rahman Khan
#

import time

def fibonacci_improved(n, depth=2, a=1, b=0, indent="", print_tree=False):
    if n == 0:
        print(f"{indent}fibonacci(0) -> 0") if print_tree else None
        return 0
    elif n == 1:
        print(f"{indent}fibonacci(1) -> 1") if print_tree else None
        return 1
    elif depth < n:
        print(f"{indent}fibonacci(n={n}, depth={depth}, a={a}, b={b})") if print_tree else None
        result = fibonacci_improved(n=n, depth=depth+1, a=a+b, b=a, indent=indent + "\t", print_tree=print_tree)
        print(f"{indent}Returning from fibonacci(n={n}, depth={depth}, a={a}, b={b}) -> {result}") if print_tree else None
        return result
    else:
        result = a + b
        print(f"{indent}Base case: fibonacci(n={n}, depth={depth}, a={a}, b={b}) -> {result}") if print_tree else None
        return result

def main(SHOW_TIME = True):
    n = 5
    time_start = time.time()
    f_num = fibonacci_improved(n)
    time_end = time.time()
    print(f"Fibonacci number at position {n}: {f_num}")
    print(f"Time taken for recursive approach: {time_end - time_start:.10f} seconds") if SHOW_TIME else None
    
main()
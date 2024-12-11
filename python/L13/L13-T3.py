# L13-T3: Fibonacci numbers
#
# Submitted by: Md Hamidur Rahman Khan
#

import time

# Naive approach
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main(SHOW_TIME = False):
    n = 30
    
    time_start = time.time()
    f_num = fibonacci(n)
    time_end = time.time()
    
    print(f"Fibonacci number at position {n}: {f_num}")
    print(f"Time taken for recursive approach: {time_end - time_start:.10f} seconds") if SHOW_TIME else None
    
main()
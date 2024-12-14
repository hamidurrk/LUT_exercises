def fibo(n):
    if n <= 1:
        return n
    fib = [0, 1] 
    for _ in range(1, n):
        fib.append(fib[-1] + fib[-2])
    return fib[n]

for i in range(10):
    print("Fibonacci of", i, "is", fibo(i))
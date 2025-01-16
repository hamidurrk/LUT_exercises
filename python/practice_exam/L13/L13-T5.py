fibo = [0, 1]

def fib(n):
    for i in range(n-1):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo[-1]

print(fib(10))
print(fibo)

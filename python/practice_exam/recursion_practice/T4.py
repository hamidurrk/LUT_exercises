def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    result = fibo(n-1) + fibo(n-2)
    return result

def fibon(n, i = 2, a = 1, b = 1):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == i:
        return b
    if n > 2:
        i += 1
        return fibon(n, i, a=b, b=a+b)

print(fibon(9))

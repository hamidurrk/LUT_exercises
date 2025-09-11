def is_prime(n: int):
    if n == 1:
        return False
    for div in range(n-1, 1, -1):
        result = n % div
        if result == 0:
            return False
    return True

def primes(N: int):
    count = 0
    while N > 0:
        if is_prime(N):
            count += 1
        N -= 1
    return count

if __name__ == "__main__":
    print(primes(7))
    print(primes(15))
    print(primes(50))
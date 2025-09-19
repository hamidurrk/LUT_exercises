def split(A):
    n = len(A)
    if n <= 1:
        return 0

    pref_max = [0] * n
    suf_min = [0] * n

    pref_max[0] = A[0]
    for i in range(1, n):
        pref_max[i] = pref_max[i - 1] if pref_max[i - 1] > A[i] else A[i]

    suf_min[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        suf_min[i] = suf_min[i + 1] if suf_min[i + 1] < A[i] else A[i]

    count = 0
    for i in range(1, n):
        if pref_max[i - 1] < suf_min[i]:
            count += 1
    return count

if __name__ == "__main__":
    print(split([1, 2, 3, 4, 5]))         
    print(split([5, 4, 3, 2, 1]))         
    print(split([2, 1, 2, 5, 7, 6, 9]))   
    print(split([1, 2, 3, 1]))            

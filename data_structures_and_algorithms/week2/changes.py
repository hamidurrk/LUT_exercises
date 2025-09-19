def changes(A):
    n = len(A)
    if n <= 1:
        return 0

    B = A.copy()
    cnt = 0
    for i in range(1, n):
        if B[i] == B[i - 1]:
            nxt = B[i + 1] if i + 1 < n else None
            for cand in (0, -1, 1001, 1002):
                if cand != B[i - 1] and cand != nxt:
                    B[i] = cand
                    break
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))  
    print(changes([1, 2, 3, 4, 5]))  
    print(changes([1, 1, 1, 1, 1]))  

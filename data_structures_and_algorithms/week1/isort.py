def isort(A: list):
    for j in range(0, len(A)-1):
        while (j >= 0) and (A[j] > A[j+1]):
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            
            j = j-1

if __name__ == "__main__":
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)

def printNos(n):
    if n == 0:
        return
    printNos(n-1)
    print(n, end=' ')

printNos(10)

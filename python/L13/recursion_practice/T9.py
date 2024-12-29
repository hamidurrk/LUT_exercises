data = 12345

def sum(data):
    if data == 0:
        return 0
    return data%10 + sum(data//10)

print(sum(data))

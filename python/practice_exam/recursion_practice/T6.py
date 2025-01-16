data = "12345"

def sum(s):
    if len(s) == 0:
        return 0
    return int(s[0]) + sum(s[1:])

print(sum(data))

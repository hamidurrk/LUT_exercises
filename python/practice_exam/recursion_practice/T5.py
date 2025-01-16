data = [1, 2, [3, 4], 5, 6]

def sum(lst):
    if len(lst) == 0:
        return 0
    if isinstance(lst[0], list):
        result = sum(lst[0]) + sum(lst[1:])
    else:
        result = lst[0] + sum(lst[1:])
    return result

print(sum(data))

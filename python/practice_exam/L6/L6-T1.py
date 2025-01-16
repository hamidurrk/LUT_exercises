in_list = [1, 2, 3, 4, 5]

def reverse(l) -> list:
    if len(l) <= 1:
        return l
    result = reverse(l[1:]) + [l[0]]
    return result

print(reverse(in_list))

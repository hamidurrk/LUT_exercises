def string_reverse(string: str):
    output = ''
    for i in range(len(string) - 1, -1, -1):
        output += string[i]
    return output

print(string_reverse("apple"))
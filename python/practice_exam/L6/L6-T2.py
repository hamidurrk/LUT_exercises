original = [1, 4, 3, 1, 5, 7, 4, -4, -12, -12, -1, -4, -4]

def remove_duplicate(lst):
    output = []

    for element in lst:
        if element not in output:
            output.append(element)
    return output

print(remove_duplicate(original))

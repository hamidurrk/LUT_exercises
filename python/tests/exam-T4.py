dict = {}

string = "1 2 3 a b aa bb 4 3 2 1 8 a"

def converter(string:str):
    list = string.split()
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    output = []
    for key, value in dict.items():
        if value == 1:
            output.append(key)
    return output

print(converter(string))
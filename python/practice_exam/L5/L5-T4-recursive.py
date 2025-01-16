def compress(string):
    def recurse(string, count = 1, count_str = ''):
        if len(string) == 1:
            count_str += f"{string[0]}{count if count > 1 else ''}"
            return count_str
        if string [0] == string[1]:
            count += 1
        else:
            count_str += f"{string[0]}{count if count > 1 else ''}"
            count = 1
        return recurse(string[1:len(string)], count, count_str)
    return recurse(string)

print(compress("aaaabbbbbbbcdddddddddeekkkkkkk"))

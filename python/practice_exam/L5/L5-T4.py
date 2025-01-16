def compress(string):
    change_list = [0]
    sliced = []
    compressed = ""
    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            change_list.append(i+1)
    change_list.append(len(string))
##    print(change_list)
    for index in range(len(change_list)-1):
        sliced.append(string[change_list[index] : change_list[index+1]])
##    print(sliced)
    for sub_slice in sliced:
        letter = sub_slice[0]
        count = len(sub_slice)
        compressed += f"{letter}{count if count > 1 else ''}"
    return compressed

print(compress("aaaabbbbbbbcdddddddddeekkkkkkk"))

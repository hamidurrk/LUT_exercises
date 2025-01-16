def compress(string):
    compressed = ""
    count = 1

    for i in range(len(string)):
        if i+1 == len(string):
            compressed += f"{string[i]}{count if count > 1 else ''}"
            break
        
        if string[i] == string[i+1]:
            count += 1
        else:
            compressed += f"{string[i]}{count if count > 1 else ''}"
            count = 1
            
    return compressed
            
        
print(compress("aaaabbbbbbbcdddddddddeekkkkkkkh"))

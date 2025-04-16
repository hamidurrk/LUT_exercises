def count_letters(s, index=0):
    """Recursively counts the number of letters in a string."""
    if index == len(s):
        return 0  
    elif s[index].isalpha():
        return 1 + count_letters(s, index + 1)
    else:
        return count_letters(s, index + 1)

print(count_letters("hello"))  
print(count_letters("hello world1234!"))
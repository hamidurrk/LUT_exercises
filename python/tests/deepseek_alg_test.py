def count_letters(s, index=0):
    """Recursively counts the number of letters in a string."""
    if index == len(s):
        return 0  # Base case: all characters processed
    elif s[index].isalpha():
        return 1 + count_letters(s, index + 1)
    else:
        return count_letters(s, index + 1)

# Example usage:
print(count_letters("hello"))  # Output: 5
print(count_letters("hello world1234!"))
words = []

words.append(input("Enter word 1:\n"))
words.append(input("Enter word 2:\n"))

if words[0] != words[1]:
    if words[0] < words[1]:
        sorter = words.copy()
    else:
        sorter = words[::-1].copy()   
    print(f"'{sorter[0]}' comes earlier in order than '{sorter[1]}'")
else:
    print("The words are the same.")

if "z" in words[0]:
    print(f"Letter 'z' is found in word '{words[0]}'")
if "z" in words[1]:
    print(f"Letter 'z' is found in word '{words[1]}'")
if "z" not in words[0] and "z" not in words[1]:
    print("Letter 'z' was not found in either of the words.")

pal_test = input("Enter a word to be tested:\n")
if pal_test == pal_test[::-1]:
    print(f"'{pal_test}' is a palindrome.")
else:
    print(f"'{pal_test}' is not a palindrome.")

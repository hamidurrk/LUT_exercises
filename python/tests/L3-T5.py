word_1 = input("Enter word 1:\n")
word_2 = input("Enter word 2:\n")

# Equality check
if(word_1 == word_2):
    print("The words are the same.")

# Order check
elif(word_1 < word_2):
    print(f"'{word_1}' comes earlier in order than '{word_2}'.")
else:
    print(f"'{word_2}' comes earlier in order than '{word_1}'.")

# 'z' check
if("z" in word_1):
    print(f"Letter 'z' is found in word '{word_1}'.")
if("z" in word_2):
    print(f"Letter 'z' is found in word '{word_2}'.")
if ("z" not in word_1 and "z" not in word_2):
    print("The letter 'z' was not found in either of the words.")

word_3 = input("Enter a word to be tested:\n")

# Palindrome check
if(word_3 == word_3[::-1]):
    print(f"'{word_3}' is a palindrome.")
else:
    print(f"'{word_3}' is not a palindrome.")
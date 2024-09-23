# L03-T5: Character string comparisons incl. palindrome testing
#
# Submitted by: Md Hamidur Rahman Khan
#

word1 = input("Enter word 1:\n")
word2 = input("Enter word 2:\n")

# Checking if the words are equal
if(word1 == word2):
    print("The words are the same.")

# Chechking which comes before the other
elif(word1 < word2):
    print(f"'{word1}' comes earlier in order than '{word2}'.")
else:
    print(f"'{word2}' comes earlier in order than '{word1}'.")

# Checking if the words contain the letter 'z'
if("z" in word1):
    print(f"Letter 'z' is found in word '{word1}'.")
if("z" in word2):
    print(f"Letter 'z' is found in word '{word2}'.")
if ("z" not in word1 and "z" not in word2):
    print("The letter 'z' was not found in either of the words.")

word3 = input("Enter a word to be tested:\n")
# Checking if word3 is a palindrome
if(word3 == word3[::-1]):
    print(f"'{word3}' is a palindrome.")
else:
    print(f"'{word3}' is not a palindrome.")
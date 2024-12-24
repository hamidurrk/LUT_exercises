word_1 = input("Enter word 1:\n")
word_2 = input("Enter word 2:\n")

if(word_1 == word_2):
    print("The words are the same.")

elif(word_1 < word_2):
    print(f"'{word_1}' comes earlier in order than '{word_2}'.")
else:
    print(f"'{word_2}' comes earlier in order than '{word_1}'.")

def z_checker(word):
    count = 0
    for x in word:
        if x == "z":
            count += 1
    if count > 0:
        return True
    return False

# print(f"{z_checker(word_1)}, and {z_checker(word_2)}")

if(z_checker(word_1)):
    print(f"Letter 'z' is found in word '{word_1}'.")
if(z_checker(word_2)):
    print(f"Letter 'z' is found in word '{word_2}'.")
if ("z" not in word_1 and "z" not in word_2):
    print("The letter 'z' was not found in either of the words.")

word_3 = input("Enter a word to be tested:\n")

# Palindrome check
if(word_3 == word_3[::-1]):
    print(f"'{word_3}' is a palindrome.")
else:
    print(f"'{word_3}' is not a palindrome.")
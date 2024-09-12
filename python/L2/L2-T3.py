# L02-T3: Cuts and length of strings
#
# Submitted by: Md Hamidur Rahman Khan
#

word = input("Enter a long word:\n")

print("First five letters are:", word[:5])
print("Last five letters are:", word[-5:])
print("Letters 2, 3, 4 and 5 are:", word[1:5])

print("Every second letter of the word:", word[1::2])
print(f"The word backwards '{word[::-1]}'")

start = int(input("Enter the start index:\n"))
end = int(input("Enter the end index:\n"))
step = int(input("Enter the step:\n"))
print(f"With these values '{word}' produces this: ", word[start:end:step])

print(f"Your word is {len(word)} characters long")

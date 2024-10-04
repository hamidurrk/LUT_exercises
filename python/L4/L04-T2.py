# L04-T2: Repetition structure with string
#
# Submitted by: Md Hamidur Rahman Khan
#

vowels_lower = ["a", "e", "i", "o", "u"]
vowels_upper = [x.upper() for x in vowels_lower]
vowels = vowels_lower + vowels_upper

input_string = input("Enter a string:\n")

count = 0
for char in input_string:
    if char in vowels:
        count += 1
print(f"The number of vowels is: {count}")
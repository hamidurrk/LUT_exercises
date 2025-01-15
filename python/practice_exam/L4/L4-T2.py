vowels = "a,e,i,o,u".split(',')
string = "The USA, the shorthand for the United States of America."

count = 0
for s_char in string.lower():
    if s_char in vowels:
        count += 1
print(count)

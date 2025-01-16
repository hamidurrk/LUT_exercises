import string, random
random.seed(8292)

COMB = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of the password:\n"))

pass_str = ''

for _ in range(length):
    pass_str += random.choice(COMB)

print(pass_str)

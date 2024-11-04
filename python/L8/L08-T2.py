# L08-T2: Continue Python library: Random
#
# Submitted by: Md Hamidur Rahman Khan
#

import string
import random

random.seed(8292)

def main():
    LETTERS = string.ascii_letters 
    DIGITS = string.digits 
    SPECIAL = string.punctuation
    COMB = LETTERS + DIGITS + SPECIAL
    
    while True:
        length = int(input("Enter the length of the password:\n"))
        if length <= 0:
            print("Password length must be a positive integer.")
        else:
            print("Generated password:", ''.join(random.choice(COMB) for _ in range(length)))
            break
main()
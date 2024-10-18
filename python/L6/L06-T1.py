# L06-T1: Reversed list
#
# Submitted by: Md Hamidur Rahman Khan
#

from L6E4 import input_integers

int_list = input_integers()
rev_list = []
for _ in range(len(int_list)):
    rev_list.append(int_list.pop())
print(f"Reversed list: {rev_list}")

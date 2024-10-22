# L06-T1: Reversed list
#
# Submitted by: Md Hamidur Rahman Khan
#

from L6E4 import input_integers

def reverse_list(int_list):
    rev_list = []
    for _ in range(len(int_list)):
        rev_list.append(int_list.pop())
    return rev_list   

int_list = input_integers()
print(f"Reversed list: {reverse_list(int_list)}")
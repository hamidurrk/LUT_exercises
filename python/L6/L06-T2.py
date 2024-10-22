# L06-T2: Removing duplicate elements from a list
#
# Submitted by: Md Hamidur Rahman Khan
#

from L6E4 import input_integers

int_list = input_integers()
tracking_list = []
for num in int_list:
    if num not in tracking_list:
        tracking_list.append(num)
print(f"Original List: {int_list}\nList with duplicates removed: {tracking_list}")
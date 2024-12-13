# L13-T6: EXTRA: Comparison of running times
#
# Submitted by: Md Hamidur Rahman Khan
#

import time
from copy import deepcopy

def read_words(file_name: str) -> list:
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
    return data

def insertionSort(li):
    for i in range(1, len(li)):
        key = li[i]
        # Move elements of li[0..i-1] that are greater than key one step back
        j = i - 1
        while j >=0 and key < li[j]:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = key    # put key into right position

def quicksort(li):
    if len(li) <= 1:  # base case
        return li
    else:
        pivot = li[0]  # first element
        below = []
        above = []
        
        for i in li[1:]:     # partitioning
            if i < pivot:
                below.append(i)
            else:
                above.append(i)
        
        return quicksort(below) + [pivot] + quicksort(above)
    
def timer_wrapper(func, data):
    time_start = time.time()
    func(data)
    time_end = time.time()
    print(f"Time taken by {func.__name__}(): {time_end - time_start:.6f} seconds")
    return time_end - time_start

    
def main():
    file_name = './python/L13/pseudo_words.txt'
    data = read_words(file_name)
    
    python_sorted_data = deepcopy(data)
    quicksort_data = deepcopy(data)
    insertion_sort_data = deepcopy(data)
    
    timer_wrapper(sorted, python_sorted_data)
    timer_wrapper(quicksort, quicksort_data)
    timer_wrapper(insertionSort, insertion_sort_data)
    
main()
import time
from copy import deepcopy

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

def insertionSort(li):
    for i in range(1, len(li)):
        key = li[i]
        # Move elements of li[0..i-1] that are greater than key one step back
        j = i - 1
        while j >=0 and key < li[j]:
            li[j+1] = li[j]
            j = j - 1
        li[j+1] = key    # put key into right position
    
def main():
    file_name = './python/L13/pseudo_words.txt'
    file = open(file_name, "r")
    data = file.readlines()
    file.close()
    
    data1 = deepcopy(data)
    data2 = deepcopy(data)
    data3 = deepcopy(data)
    
    time_start = time.time()
    sorted(data1)
    time_end = time.time()
    print(f"Time taken by sorted(): {time_end - time_start:.6f} seconds")
    
    time_start = time.time()
    quicksort(data2)
    time_end = time.time()
    print(f"Time taken by quicksort(): {time_end - time_start:.6f} seconds")
    
    time_start = time.time()
    insertionSort(data3)
    time_end = time.time()
    print(f"Time taken by insertionSort(): {time_end - time_start:.6f} seconds")
    
main()
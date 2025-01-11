import random  # for filling the list
import time    # for performance measure

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

test1 = [] # test array
test2 = [] # test array

size = 30000

for i in range(size):
    N = random.randint(0, 10*size) # fill the array with random elments
    test1.append(N)
    test2.append(N)


# Test for insertion sort    
timer1 = time.time()
insertionSort(test1)
timer2 = time.time()
duration = timer2 - timer1
print(f"Insertion sort took {duration:.2f} seconds")

# Test for quicksort    
timer1 = time.time()
out = quicksort(test2)
timer2 = time.time()
duration = timer2 - timer1
print(f"Quicksort took {duration:.2f} seconds")





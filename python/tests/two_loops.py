import time

n = 10000
k = 0

start_time = time.time()   

for i in range(n):
    for j in range(n):
        k = k + i + j
 
end_time = time.time()  

running_time = end_time - start_time
print(f"With the size of n = {n}, the running time is {running_time:.3f} seconds")

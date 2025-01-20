string = "1 2 3 a b aa bb 4 3 2 1 1 a 8 a"

lst = string.split()
pop_index = []

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst[j] and i != j:
            pop_index.append(lst[i])

for value in pop_index:
    if value in lst:
        lst.remove(value)
        
print(lst)
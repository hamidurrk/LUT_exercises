start = int(input("Enter the starting value:\n"))
end = int(input("Enter the ending value:\n"))

print("Implementation with a for loop:")
for i in range(start, end + 1):
    if i == end:
        print(i)
    else:
        print(i, end=" ")
    
print("Implementation with a while loop:")
i = start
while True:
    if i == end:
        print(i)
        break
    else:
        print(i, end=" ")
    i += 1
    

# L04-T1: Different repetition structures 
#
# Submitted by: Md Hamidur Rahman Khan
#

start_value = int(input("Enter the starting value:\n"))
end_value = int(input("Enter the ending value:\n"))

print("Implementation with a for loop:")
for i in range(start_value, end_value+1):
    if not i == end_value:
        print(i, end=" ")
    else:
        print(i)

print("Implementation with a while loop:")
count = start_value
while count <= end_value:
    if not count == end_value:
        print(count, end=" ")
    else:
        print(i)
    count += 1
# L05-T3: Function with parameters, string check
#
# Submitted by: Md Hamidur Rahman Khan
#

def is_containing(part, container):
    count = 0
    for i in range(len(container)):
        for j in range(len(part)):
            if i < len(container):
                # print(container[i], part[j])
                if container[i] == part[j]:
                    count += 1
                    i += 1
                else:
                    count = 0
        if count == len(part):
            return True
    return False
   
        
# print(isContaining("tea", "teat"))

string_input = "part"
container_input = "apartment"

# string_input = input("Enter the first string:\n")
# container_input = input("Enter the second string:\n")

FOUND = is_containing(string_input, container_input)

if FOUND:
    print("The first string can be found in the second string.")
else:
    print("The first string cannot be found in the second string.")
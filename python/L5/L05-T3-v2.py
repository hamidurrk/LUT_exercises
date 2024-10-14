# L05-T3: Function with parameters, string check
#
# Submitted by: Md Hamidur Rahman Khan
#

def substring_search(container, string):
    container_len = len(container)
    string_len = len(string)
    
    for i in range(container_len - string_len + 1):
        match = True
        for j in range(string_len):
            if container[i + j] != string[j]:
                match = False
                break
        if match:
            return True
    return False
        

string_input = input("Enter the first string:\n")
container_input = input("Enter the second string:\n")

FOUND = substring_search(string=string_input, container=container_input)

if FOUND:
    print("The first string can be found in the second string.")
else:
    print("The first string cannot be found in the second string.")
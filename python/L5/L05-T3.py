# L05-T3: Function with parameters, string check
#
# Submitted by: Md Hamidur Rahman Khan
#

def isContaining(string : str, container: str):
    string_index_match_list, container_index_match_list = [], []
    for x in range(len(container)):
        for y in range(len(string)):
            if container[x] == string[y]:
                # if not string_index_match_list or y == string_index_match_list[-1] + 1:
                container_index_match_list.append(x)
                string_index_match_list.append(y)
                print(x, container[x], string[y], y)
    print(string_index_match_list)
    print(container_index_match_list)
    match_count = 0
    
    if all(container_index_match_list[i] - container_index_match_list[i-1] == 1 for i in range(1, len(container_index_match_list))) and len(container_index_match_list) == len(string):
        for x in range(len(string_index_match_list)):
            # print(len(string_index_match_list))
            # print(x)
            # print("iterating")
            if string_index_match_list[x] == 0:
                # print("match found")
                count = 0
                for i in range(len(string)):
                    # print(string_index_match_list[x+i], count)
                    if x+i < len(string_index_match_list):    
                        if string_index_match_list[x+i] == count:
                            print(count, string_index_match_list[x+i])
                            match_count += 1
                    count += 1
        print(match_count)
        
        if match_count == len(string):
            return True
        
    return False
    
        
# print(isContaining("tea", "teat"))

string_input = "part"
container_input = "apartment"

# string_input = input("Enter the first string:\n")
# container_input = input("Enter the second string:\n")

FOUND = isContaining(string_input, container_input)

if FOUND:
    print("The first string can be found in the second string.")
else:
    print("The first string cannot be found in the second string.")
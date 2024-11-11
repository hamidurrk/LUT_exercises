# L09-T2: Exception handling with file read & write
#
# Submitted by: Md Hamidur Rahman Khan
#

def process_file(file_name, process_function, content=[], mode="r"):
    try:
        file = open(file_name, mode)
        return process_function(file, content)
    except:
        print(f"Error processing file '{file_name}'.")
        return None

def read_file(file, content=[], count=0):
    line = file.readline()
    if line == "":
        file.close()
        print(f"File '{file.name}' read successfully, {count} lines.")
        return content
    count += 1
    content.append(int(line))
    return read_file(file, content, count)

def write_file(file, content=[]):
    for line in content:
        file.write(f"{line}\n")
    file.close()
    print(f"File '{file.name}' was successfully written.")

def menu():
    source = input("Enter the name of the file to be read:\n")
    content = process_file(source, read_file, mode="r")
    if content != None:
        destination = input("Enter the name of the file to be written:\n")
        process_file(destination, write_file, content, mode="w")
    
menu()
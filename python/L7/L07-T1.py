# L07-T1: Reading & Writing text files
#
# Submitted by: Md Hamidur Rahman Khan
#

def file_write(name: str):
    file = open(name, mode="w")
    while True:
        input_string = input("Enter a name to save to the file (0 to stop):\n")
        if input_string == "0":
            break
        file.write(input_string + "\n")
    file.close()

def file_read(name: str):
    file = open(name, mode="r")
    print(f"The following names are stored in the file '{name}'")
    for line in file.readlines():
        print(line.strip())
    file.close()
    
def main():
    name = input("Enter the name of the file to be saved:\n")
    file_write(name)
    file_read(name)

if __name__ == "__main__":
    main()
    # file_read("Exercise1.txt")
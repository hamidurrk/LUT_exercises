def file_read(name):
    file = open(name, 'r')
    print(f"The following names are stored in the file '{name}':")
    while True:
        data = file.readline()
        if data == "":
            break
        print(data.strip())
    file.close()

def file_write(name):
    file = open(name, 'w')
    while True:
        data = input("Enter a name to save to the file (0 to stop):\n")
        if data == "0":
            break
        file.write(data+'\n')
    file.close()

def main():
    name = input("Enter the name of the file to be saved:\n")
    file_write(name)
    file_read(name)

main()

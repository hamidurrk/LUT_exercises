def file_copy(fileA, fileB):
    source = open(fileA, 'r')
    destination = open(fileB, 'w')

    while True:
        data = source.readline()
        if data == "":
            break
        destination.write(data)
    source.close()
    destination.close()
    print("File copied successfully!")

source = input("Please give the name of the source file:\n")
destination = input("Please give the name of the destination file:\n")

file_copy(source, destination)

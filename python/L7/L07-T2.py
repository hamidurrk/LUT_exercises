# L07-T2: Copying from one file to another
#
# Submitted by: Md Hamidur Rahman Khan
#

def file_copy(fileA: str, fileB: str):
    source = open(fileA, "r")
    destination = open(fileB, "w")
    for line in source.readlines():
        destination.write(line)
    source.close()
    destination.close()
    print("File copied successfully!")

def main():
    fileA = input("Please give the name of the source file:\n")
    fileB = input("Please give the name of the destination file:\n")
    file_copy(fileA=fileA, fileB=fileB)

if __name__ == "__main__":
    main()
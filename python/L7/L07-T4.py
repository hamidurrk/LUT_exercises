# L07-T4: CSV file
#
# Submitted by: Md Hamidur Rahman Khan
#

def get_col(file_name: str, col_num: int):
    csv_file = open(file_name, "r")
    col = []
    for line in csv_file.readlines():
        col.append(line.strip().split(",")[col_num-1].strip())
    csv_file.close()
    return col

def main():
    file_name = input("Give the name of the CSV file:\n")
    for value in get_col(file_name=file_name, col_num=2):
        print(value)   
if __name__ == "__main__":
    main()
def get_column(name, col = 2):
    file = open(name, 'r')
    data = file.readlines()
    col_data = []
    for line in data:
        line = line.split(",")
        line = [x.strip() for x in line]
        col_data.append(line)

    for line in col_data:
        print(line[col-1])
    
name = input("Give the name of the CSV file:\n")
get_column(name)

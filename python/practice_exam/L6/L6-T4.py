def create_matrix(rows, cols):
    matrix = []
    for i in range(1, rows + 1):
        while True:
            row_input = input(f"Give row {i}:\n")
            row_data = row_input.split()
            if len(row_data) != cols:
                print("Error: Invalid number of elements in the row. Please try again.")
            else:
                break
        matrix.append([int(x) for x in row_data])
    return matrix

def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        print("|", end='')
        for j in range(cols):
            if j == cols-1:
                end = ''
            else:
                end = '\t'
            print(matrix[i][j], end=end)
        print("|")

def main():
    rows = int(input("Enter the number of rows:\n"))
    cols = int(input("Enter the number of cols:\n"))
    matrix = create_matrix(rows, cols)
    print_matrix(matrix)
            
main()

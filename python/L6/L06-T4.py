# L06-T4: Matrix
#
# Submitted by: Md Hamidur Rahman Khan
#

# matrix = {(0, 0): '1', (0, 1): '2', (0, 2): '3', 
#           (1, 0): '1', (1, 1): '2', (1, 2): '3'}

def create_matrix(rows:int = 2, cols:int = 3):
    matrix = {}
    for m in range(rows):
        while True:
            values = input(f"Give row {m+1}:\n")
            values = values.split()
            if not len(values) == cols:
                print("Error: Invalid number of elements in the row. Please try again.")
            else:
                break
        for n, val in enumerate(values):
            matrix.update({(m, n): val})
    return matrix

def print_matrix(matrix:dict):
    m, n = max(matrix.keys())
    for i in range(m+1):
        print("|", end="")
        for j in range(n+1):
            print(matrix[(i, j)], end="" if j==n else "\t")
        print("|")
    
def main():
    rows = int(input("Enter the number of rows:\n"))
    cols = int(input("Enter the number of columns:\n"))
    matrix = create_matrix(rows=rows, cols=cols)
    print_matrix(matrix)
    
if __name__ == "__main__":
    main()
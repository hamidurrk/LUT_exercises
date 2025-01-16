matrix = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
]

def exception_handler(fun):
    try:
        fun()
    except IndexError:
        print("IndexError occured!")
    except ValueError:
        print("ValueError occured!")

def get_input():
    row = int(input("Enter the row index:\n"))
    col = int(input("Enter the column index:\n"))

    print(f"Value at {row}, {col}: {matrix[row][col]}")

exception_handler(get_input)

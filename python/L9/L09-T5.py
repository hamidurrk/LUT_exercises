# L09-T5: Matrix
#
# Submitted by: Md Hamidur Rahman Khan
#

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def get_position():
    row = int(input("Enter the row index:\n"))
    col = int(input("Enter the column index:\n"))

    value = matrix[row][col]
    print(f"Value at position ({row}, {col}): {value}")
    
def exception_handler(subroutine, *args):
    try:
        subroutine(*args)
    except IndexError:
        print("Error: Index out of bounds. Please enter valid row and column indices.")
    except ValueError:
        print("Error: Please enter valid integers for row and column indices.")

exception_handler(get_position)
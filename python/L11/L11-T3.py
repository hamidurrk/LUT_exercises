# L11-T3: Matrix 1
#
# Submitted by: Md Hamidur Rahman Khan
#

import numpy as np

class Matrix:
    instance_count = 0
    def __init__(self):
        Matrix.instance_count += 1
        ordinal = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth'}
        matrix = []
        rows = int(input(f"Enter the number of rows for the {ordinal[Matrix.instance_count]} matrix:\n"))
        cols = int(input(f"Enter the number of columns for the {ordinal[Matrix.instance_count]} matrix:\n"))
        print(f"Enter values for a {rows}x{cols} matrix:")
        for m in range(rows):
            while True:
                values = input(f"Enter {cols} values for row {m+1} (separated by space):\n")
                values = values.split()
                if not len(values) == cols:
                    print("Error: Invalid number of elements in the row. Please try again.")
                else:
                    break
            matrix.append([float(val) for val in values])
        self.matrix = np.array(matrix)
        print(f"This is matrix {Matrix.instance_count}:")
        self.print_matrix()
    
    def print_matrix(self):
        print(self.matrix)
    
    def get_matrix(self):
        return self.matrix

    def add(self, matrix2):
        matrix2 = matrix2.matrix
        if self.matrix.shape == matrix2.shape:
            matrix_sum = self.matrix + matrix2
            print("Matrix sum:")
            print(matrix_sum)
        else:
            print("Error: sum not possible")

    def multiply(self, matrix2):
        matrix2 = matrix2.matrix
        if self.matrix.shape[1] == matrix2.shape[0]:
            matrix_product = np.dot(self.matrix, matrix2)
            print("Matrix multiplication:")
            print(matrix_product)
        else:
            print("Error: multiplication not possible")

mat1 = Matrix()
mat2 = Matrix()

mat1.add(mat2)
mat1.multiply(mat2)

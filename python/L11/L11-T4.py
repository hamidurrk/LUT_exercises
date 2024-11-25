# L11-T4: Matrix 2
#
# Submitted by: Md Hamidur Rahman Khan
#

import numpy as np

class Matrix:
    def __init__(self):
        print("This program demonstrates use of numpy-matrix.")
        self.rows = int(input("Enter amount of rows:\n"))
        self.cols = int(input("Enter number of columns:\n"))
        self.matrix = self.create_zero_matrix()
        
    def create_zero_matrix(self):
        matrix = np.zeros((self.rows, self.cols), dtype=int)
        print("Zero-matrix of the given rows & columns is:")
        print(' ', end='')
        print(matrix)
        return matrix
    
    def fill_matrix(self):
        matrix = self.matrix
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                matrix[row, col] = (row + 1) * (col + 1)
        print("Matrix printed with np-formatting:")
        print(matrix)
        print("")
        self.matrix = matrix
        
    def sort_matrix(self):
        matrix = self.matrix
        sorted_matrix = np.sort(matrix, axis=None)
        print("Matrix sorted into one array:")
        print(sorted_matrix)
        
    def print_matrix_with_semicolons(self):
        matrix = self.matrix
        print("Matrix printed with elements separated by semicolons:")
        for row in matrix:
            print(";".join(map(str, row)) + ";")
        print("")
        
    def reshape_matrix(self):
        matrix = self.matrix
        while True:
            try:
                print("Shaping the matrix. Please, enter the new dimensions.")
                new_rows = int(input("Enter amount of new rows:\n"))
                new_cols = int(input("Enter amount of new columns:\n"))
                if new_rows * new_cols != matrix.size:
                    print("Faulty shape. Please, try again.")
                else:
                    reshaped_matrix = matrix.reshape((new_rows, new_cols))
                    print("Newly shaped matrix is:")
                    print(' ', end='')
                    print(reshaped_matrix)
                    self.reshaped_matrix = reshaped_matrix
                    return reshaped_matrix
            except ValueError:
                print("Invalid input. Please enter integers.")
    def matrix_statistics(self):
        matrix = self.matrix
        print(f"Largest number in the matrix is: {matrix.max()}")
        print(f"Smallest number in the matrix is: {matrix.min()}")
        print(f"Sum of all values in the matrix is: {matrix.sum()}")

    def process_list(self):
        list_values = [int(item) for item in input("Enter the list items:\n").split()]
        unique_values = np.unique(list_values)
        print("Unique values are:", unique_values)
        
    def main(self):
        self.fill_matrix()
        self.sort_matrix()
        self.print_matrix_with_semicolons()
        self.reshape_matrix()
        self.matrix_statistics()
        self.process_list()

mat = Matrix()
mat.main()

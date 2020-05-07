class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for n in range(len(other.matrix[0])):
                self.matrix[i][n] = self.matrix[i][n] + other.matrix[i][n]
            result = self.matrix
        return Matrix(result)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in self.matrix]))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print('*' * 6)
print(matrix_2)
print('*' * 6)
print(matrix_1 + matrix_2)

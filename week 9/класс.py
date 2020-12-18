from sys import stdin
import numpy as np

class Matrix(list):
    def __init__(self, matrix):
        self.matrix = [line.copy() for line in matrix]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, matrix):
        return np.array(self.matrix) + np.array(matrix)

    __rmul__ = __mul__

    def __mul__(self, const):
        return np.array(self.matrix) * const


exec(stdin.read())

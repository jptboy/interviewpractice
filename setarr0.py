"""
Problem: Write a function that accepts an m x n matrix (array) of random numbers, 
and use the functions row (times) 2 and column-1 to set the entire array to 0.

Source: https://github.com/CourtneyThurston/microsoft-internships
"""
import random
import time
import numpy as np

def row2(mat,i):
    for j in range(len(mat[i])):
        mat[i][j] *= 2

def col1(mat,j):
    for i in range(len(mat)):
        mat[i][j] -= 1

def colNotSameVals(matrix, j):
    v = matrix[0][j]
    for i in range(len(matrix)):
        if matrix[i][j] != v:
            return True
    return False

def set0(matrix):
    for col in range(len(matrix[0])):
        while colNotSameVals(matrix,col):
            for i in range(len(matrix)):
                if matrix[i][col] == 1:
                    row2(matrix, i)
            col1(matrix, col)
        v = matrix[0][col]
        for _ in range(v): col1(matrix,col)

upper = 4
upperN = 4
n = random.randint(3,upper)
m = random.randint(3,upper)
        
matx = [[random.randint(1,upperN) for j in range(n)] for i in range(m)]

print(np.matrix(matx))
set0(matx)
print('---')
print(np.matrix(matx))
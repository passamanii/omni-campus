import numpy as np


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

a = np.array(a)

print("Advanced Indexing (Termo 5):", a[[1],[1]])
print("Advanced Indexing (Termos 3, 4, 7):", a[[0, 1, 2], [2, 0, 0]])

print("Advanced Indexing (Termos 1, 7, 3, 9)", a[[[0], [2]], [0, 2]])
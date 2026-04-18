import numpy as np

a = [[1, 2, 3],
     [4, 5, 6]]

#Axis 0 = Columns (Agrupa em Colunas)
#Axis 1 = Rows (Agrupa em Linhas)

print(a)
print("Max da Axis 1:", np.max(a, axis=1))
print("Max da Axis 0:", np.max(a, axis=0))

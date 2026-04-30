import numpy as np


a = [[1, 2],
     [2, 3],
     [3, 4]]
a = np.array(a)

#Atualmente a é uma matriz de forma 2X2

a = a.reshape(1, -1) #Colocar -1 como índice, faz com que o programa decida o tamanho ideal de elementos em cada linha

print(a)
print("\n")
print(a.reshape(3, -1))
print("\n")
print(a.reshape(6, -1))
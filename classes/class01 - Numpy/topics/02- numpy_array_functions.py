import numpy as np

x = [0, 2, 4, 6]
y = [1, 3, 5, 7]
z = [[1, 2, 3, 4], [5, 6, 7, 8]]

print("X: ", x)
print("Y: ", y)
print("Z: ", z)

print("Lista Python:")
print("X+Y: ", x+y)

x = np.array(x)
y = np.array(y)
z = np.array(z)

print("Lista Numpy:")
print("X+Y: ", x+y)

print("X * Z ", x*z)
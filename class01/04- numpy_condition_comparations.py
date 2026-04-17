import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]

print("Python:")
print("A = B?", a == b)
print("A = A?", a == a)

print("Numpy:")
print("A = B?", np.equal(a, b))
print("A = A?", np.equal(a, a))

print("A < B?", np.less(a, b))
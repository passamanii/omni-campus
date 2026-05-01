import numpy as np

#(1) Create two 1-dimensional np.ndarray arrays with your favorite values as elements, and use the type() function to confirm that they are of type np.ndarray.

a = [2, 4, 6, 8]
b = [1, 3, 5, 7]

a = np.array(a)
b = np.array(b)

print(f"Type of a: {type(a)}")
print(f"Type of b: {type(b)}")

#(2) Perform arithmetic operations on the two 1-dimensional arrays created in (1).

a *= 2
b -= 2

print(f"a: {a}")
print(f"b: {b}")
print(f"a * b: {a*b}")


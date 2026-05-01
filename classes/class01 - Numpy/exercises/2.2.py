import numpy as np

#(1) For any array you create, retrieve and display the first value from the front and the first value from the back.

a = np.array([1, 2, 3, 4, 99])
print(f"First value from the front: {a[0]}")

print(f"First value from the back: {a[-1]}")

#(2) Implement a function that takes a one-dimensional Numpy array with integer values as an argument and outputs an array containing elements that are either odd (leave a remainder of 1 when divided by 2) or leave a remainder of 2 when divided by 4.

def make_bool_ids(a):
    b = a[(a % 2 == 1) | (a % 4 == 2)]
    return b

a = np.array([1, 2, 3, 4, 5, 10, 14, 20])
b = make_bool_ids(a)
print(b)


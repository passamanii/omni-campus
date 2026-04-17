import numpy as np
import random as r

def fill_array(rows, columns, array):

    for i in range(0, rows):
        array.append([])
        k = 0
        for j in range(0, columns):
            array[i].append(r.randint(0, 1000))
            if (k == 3):
                print(f"{array[i]}\t")
            k += 1

def teste():
    x = []

    fill_array(10, 4, x)

def learn():

    x = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
    
    x = np.array(x)
    idx = (x == 3)

    print("Array:\n", x)
    print("Boolean:\n", idx)

learn()
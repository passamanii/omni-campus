import numpy as np

def main():
    x = [1, 2, 3, 4, 5, 7]
    x = np.array(x)

    print("Array X: ", x)
    print("Tipo de X: ", type(x))
    
    x = x.tolist()
    print("Array X: ", x)
    print("Tipo de X: ", type(x))

main()
import numpy as np

def homework(a):
    
    my_result = a[(a % 5 == 0) & (a % 2 == 1)] # As condições vão gerar um array booleano. Esse resultante será utilizado como uma máscara pelo operador "a[mask]", copiando os elementos em que é encontrado o estado TRUE e ignorando os em que é encontrado FALSE.

    return my_result

def main():

    array = [1, 2, 15, 25, 35, 55]
    array = np.array(array)

    result = homework(array)

    print(result)

main()
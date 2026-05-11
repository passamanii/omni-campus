import pandas as pd

# Existem dois tipos de estruturas de dados em pandas:

# Series: pd.Series
# 1 dimensão
# É acompanhada de índices (linhas)
# Index : Value

series = pd.Series([1, 2, 3.5, 4, 7])
print(f"\nSeries: \n\n{series}")

# Personalizar os indices

print("\n-------------------------------------------")
series2 = pd.Series([1, 2, 3, 4, 5],
index = ['a', 'b', 'c', 'd', 'e'])
print(f"\nSeries Index Modified: \n\n{series2}")

# Data Frame: pd.DataFrame
# N dimensões
# É acompanhada, além de índices(linhas), de labels(colunas)

data = {
    "ID":[100, 101, 102, 103],
    "City": ["Nebraska", "Massachussets", "São Paulo", "Curitiba"], 
    "Birth Year":[1992, 1995, 2010, 2005],
    "Name": ["Christoff Braptlov", "Sarah Uruskhr", "João Ferraz", "Luís Passamani"]
}

data_frame = pd.DataFrame(data)
data_frame2 = pd.DataFrame(data, index=['lets', 'get', 'going', 'to partyyy'])

print("\n-------------------------------------------")
print(f"\nData Frame:\n")
print(data_frame)
print(f"\n")

print("\n-------------------------------------------")
print(f"\nData Frame Index Modified:\n")
print(data_frame2)
print(f"\n")

print("\n-------------------------------------------")
print("\nData Frame Printed With 'N' Lines:\n")
print(data_frame.head(2))
print(f"\n")


#Ejercicio 2
# Realizá un programa que compare (si son mayores, menores o iguales) los
# elementos de dos series de números de Pandas.

import pandas as pd
serie1 = pd.Series([3, 7, 9, 14, 25], dtype = int)
serie2 = pd.Series([1, 7, 10, 16, 19], dtype = int)

print(serie1 > serie2)
print(serie1 == serie2)
print(serie1 < serie2)
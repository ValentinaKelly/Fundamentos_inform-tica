#Ejercicio 1
# Escribí un programa que sume, reste, multiplique y 
# divida dos series de números de Pandas.

import pandas as pd

serie1 = pd.Series([3, 7, 12, 15, 21], dtype = int)
serie2 = pd.Series([1, 4, 10, 14, 19], dtype = int)


seriesuma = serie1 + serie2
serieresta = serie1 - serie2
seriemulti = serie1 * serie2
seriedivi = serie1/serie2

print(seriesuma)
print(serieresta)
print(seriemulti)
print(seriedivi)

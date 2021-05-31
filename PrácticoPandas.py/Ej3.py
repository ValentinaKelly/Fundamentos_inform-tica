#Ejercicio 3
#Escribí un programa para convertir
#un diccionario a una serie de Pandas

import pandas as pd
dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e":50}
lista1 = []
lista2 = []
lista3 = []
lista4 = []
for keys in dict1:
    lista1.append(dict1[keys])
#como una serie
serie1 = pd.Series(lista1, dtype = int)
print(serie1)

#Segunda alternativa en caso de tener que meter todo como data frame
contador = 0
for i in dict1.values():
    contador +=1
    lista3.append(i)
    contador += 1 
    lista4.append(contador)
letras_numeros = pd.DataFrame(data ={'letra':[lista3], 'numero':[lista1]}, index = lista4 )
print(letras_numeros)

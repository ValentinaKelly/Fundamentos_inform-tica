#https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Introduccion_a_Ciencia_de_datos/Pr%C3%A1ctica_pandas_1.md

#Ejercicio 1
# Escribí un programa que sume, reste, multiplique y 
# divida dos series de números de Pandas.

import pandas as pd
'''
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


#Ejercicio 2
# Realizá un programa que compare (si son mayores, menores o iguales) los
# elementos de dos series de números de Pandas.

serie1 = pd.Series([3, 7, 9, 14, 25], dtype = int)
serie2 = pd.Series([1, 7, 10, 16, 19], dtype = int)

print(serie1 > serie2)
print(serie1 == serie2)
print(serie1 < serie2)



#Ejercicio 3
#Escribí un programa para convertir
#un diccionario a una serie de Pandas
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

'''
#Ejercicio 4
#Escribí un programa que dado un diccionario cuyos valores son listas de números, cree otro diccionario con las mismas claves, pero donde los valores sean una lista de números donde se potencia un número por el siguiente, tomándolos de a pares. Para ser más claros miremos este ejemplo donde si un diccionario es:
#dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
#el diccionario resultante debería ser:
#dict2 = {"a": [1, 25], "b": [16, 27]}
#Esto se obtiene al hacer 1 al cubo (el primer par de la lista "a"), y 5 al cuadrado, por un lado; y 4 al cuadrado y 3 al cubo por el otro. Se considera que la cantidad de elementos en las listas siempre es par, por lo que no habría que hacer ninguna comprobación al respecto. Se puede usar el dict1 como diccionario de muestra, pero considerá
#que la lista puede ser más grande. Por último hay que convertir este último diccionario en un DataFrame de Pandas.

dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
dict2 = {}

for clave in dict1.keys():
    dict2[clave]=[]
    for numero in dict1[clave]:
        if dict1[clave].index(numero)%2==0:
            dict2[clave].append(numero**dict1[clave][(dict1[clave].index(numero))+1])
print(dict2)

#Otra forma de hacerlo 
for clave, valor in dict1.items():
    pares = []
    impares = []
    potencias = []
    for i in range(len(valor)):
        if i % 2 == 0:
            pares.append(valor[i])
        else:
            impares.append(valor[i])
    for i in range(len(pares)):
        potencias.append(pares[i]**impares[i])
    dict2[clave]= potencias
print(dict2)
new_df = pd.DataFrame(dict2)
print(new_df)






#sep() Indica cómo separar los elementos. Por defecto es la coma ",", pero se puede modificar
#header(): Selecciona una fila como encabezado.
#dtype(): indica el tipo de datos del df
#skiprows(): ignora un número de filas. Por defecto es cero
#nrows(): cantidad de líneas que se leen del archivo. Sirve cuando el archivo es muy grande
#df.head(): muestra un nro dado de la parte inicial del df
# df.tail(): muestra un nro dado del final del df
# df.max(): nos dice el valor máximo por columna
# df.min(): el valor minimo 
# df.count(): devuelve la cant de datos no nulos de cada columna

#Varificar condiciones por columna de un df
#Ejemplo: imprimir los valores de todas las columnas, cuyas filas sean mayores a 0 en la columna A:
datos = {'A': [-1, 54, -4, 5], 'B':[7,91,-46,8], 'C':[18,93,0,1]}
df = pd.DataFrame(datos)
print(df)
#Selecciona las filas que no tengan elementos en las columnas menores a cero, o sea negativos. 
#Uniones con pandas.concat():
#Se pueden concatenar objetos de manera de unirlos generando nuevas columnas o filas
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B':['B0', 'B1', 'B2', 'B3'], 'C':['C0', 'C2', 'C3'], 'D':['D0', 'D1', 'D2', 'D3']}, index=[0,1,2,3])
df2 = pd.DataFrame({'B':['B2', 'B3', 'B6', 'B7'], 'D':['D2', 'D3','D6','D7'], 'F':['F2','F3','F6','F7']}, index=[2,3,6,7])
#Explicita los índices con index(), serán los índices de las filas 
result = pd.concat([df1, df2])
#axis = 0 trabaja en el eje de las columnas
result=pd.concat([df1, df2], axis=1)
#En lugar de repetirme los índices ahora me repitió las columnas. Se unen los df al costado y no debajo. 

#Si quiero la intersección de los dfs hago:
result = pd.concat([df1, df2], join='inner')
#inner me da la intersección entre los df, lo que coincide entre ellos. 

#pd.append(): anterior a concat(), no modifica el df
result = df1.append(df2)

#Para unir dos df e ignorar índices en las filas para que sean consecutivas
result = pd.concat([df1,df2], ignore_index = True, sort=False)
result = df1.append(df2, ignore_index=True, sort=False)

#Concatenar df con series:
s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name = 'X')
result = pd.concat([df1, s1], axis=1)

#Añadir una serie como una nueva fila con append():
s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=[1, 'B', 'C', 'D'])
result = df.append(s2, ignore_index=True)

#Df como diccionarios:
print(df1.to_dict())
#Nos devuelve la clave del diccionario y otro diccionario dentro, donde
#  los valores de ese son el índice y el valor del índice. 

#Series a listas:
print(s2.to_list())
print(s2.to_dict())


#Ejercicio 7
#Creá un programa que dado un diccionario y una lista añada está última al DataFrame generado a partir del diccionario.
import pandas as pd
from numpy import inner
Dic = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
Lista = [10, 20, 30, 40, 50]

df = pd.DataFrame(Dic)
'''df.assign(Lista = Lista)
print(df.assign(Lista = Lista)) #Inserta la lista como columna'''

result = df.append(Lista, ignore_index=True )
print(result)




#Ejercicio 8
#Realizá un programa que dado dos DataFrames genere otro que contenga solo las columnas en común.
Dic1 = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
Dic2 = {1: [6, 7, 8, 9], 2:[10, 11, 12, 13], 4: [14, 15, 16, 17]}
df1 = pd.DataFrame(Dic1)
df2 = pd.DataFrame(Dic2)

concatenados = pd.concat([df1, df2], axis=0)
print(concatenados.reset_index())
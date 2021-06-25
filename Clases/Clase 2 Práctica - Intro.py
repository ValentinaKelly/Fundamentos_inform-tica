#elif: else + if
'''
if condición1: órdenes si la condición1 es verdadera
else:
    if condición2: órdenes si la condición2 es verdadera

if condición1: órdenes si la condición1 es verdadera
else:
   if condición2: órdenes si la condición es verdadera
else: órdenes si ninguna es verdadera

if condicion1
elif condicion2: órdenes si la condición 1 es falsa y la condición 2 es verdadera
else: órdenes si ninguna es verdadera
'''

#Repeticiones
'''
for: cuando se sabe la cant de repeticiones que se van a dar
for variable in iterable: ordenes a repetir. 
iterable: strings, range, lista, diccionario
'''
for letra in "hola":
    print(letra)

#Sin saber la cant de repeticiones: while
#while condición: #órdenes a repetir.
#Dentro de las órdenes que se repiten debe haber una que modifique la condición, a fin de evitar un bucle infinito


#Diccionarios
dict1 = {"uno": 1, "dos": 2, "tres": 3}
for clave in dict1.keys() :
    print(clave)

for clave,valor in dict1.items() :
    print(clave, valor)
    
for valor in dict1.values() :
    print(valor)


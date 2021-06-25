#Desafío 7: Después de tanto programar necesitamos unos matecitos. Hoy aprendiste a prepararlos. Lo que no estoy segura es de que el agua alcance para toda la ronda. Suponiendo que cada cebada de mate consume 30 ml de agua. Construí una función que nos permite calcular cuántos termos de 1000 ml llenos consumiremos para una ronda dada (es decir una cantidad de personas dada).
def vaquita (precio,personas):
    return precio/personas

print(vaquita(240,6))
#40.0

#Desafío 6: Si hacemos una vaquita ? Vaquita se le dice en Argentina a hacer una colecta de plata para un fin común. Crea una función que nos permita dividir los costos de una docena de facturas entre cierta cantidad de comensales.
def mate(personas):
    return int(1000 / ((personas) * 30))

print(mate(10))
#3

'''
Síndrome de Diógenes: es una patología donde la gente acumula cosas. Se declaran listas utilizando corchetes, dentro de los corchetes separo los diferentes elementos con coma. Las listas son mutables, se pueden cambiar, a diferencia de los strings. Con len podemos conocer la longitud de la lista, o sea la cant de elementos que tiene. 

lista.append( “25” ): para agregar un elemento de la lista
lista.remove(“2”) : para remover elementos de la lista
lista.index(“25”): permite saber en qué posición tengo el elemento que estoy pasando, acordarse que python cuenta a partir de cero
floats: números con coma o decimales. 

Diccionarios: permite almacenar datos, y son mutables, pero a diferencia de las listas, no tienen un orden, no hay tal índice. Las podrá ser cualquier objeto inmutable. vendría a ser como una categoría, el valor puede ser cualquier tipo de dato, la llave sería la categoría y el valor sería el elemento que va en esa categoría. por ejemplo uso comidas = { } y luego comidas[“frutas”] = [“pera”, “banana”] y los meterá en la categoría de comidas frutas. 
diccionario = {0}
diccionario = dic{ }
diccionario.keys(): para saber cuántas llaves tiene el diccionario
diccionario.value() : te dice como está ordenado el diccionario
len(diccionario()) : te dice cuántas listas hay, cuántas categorías
Si a una llave le agrego un número entre corchetes, lo estoy poniendo en ese orden 
'''
#Librería RE: https://docs.python.org/3/library/re.html
#Expresiones regulares: para filtrar bases de datos, para aproximar cosas. Filtrar tablas con texto y números. 
# Las expresiones regulares son cadenas de caracteres basadas en reglas sintácticas, que permiten describir secuencias de caracteres

#Metacaracteres: Formato para escribir en lenguajes de 
# programación sin que se vea una vez que se publica pero que para hacerlo es necesario

# ^ Inicio de línea
# $ Fin de linea
# \A Inicio de texto
# \Z Fin de texto
# . Coincide con cualquier caracter en una línea dada

#Bibliotecas: conjunto de programas ya hechos en python, que te dejan manipular varios datos, y también podes importarlos a donde estás trabajando. Por ejemplo pandas.
import re #biblioteca que usamos para ER, se debe importar en python y siempre que se la vaya a usar, no queda “guardada”.

# \n salto de línea
# \t Tab o cambio de pestaña
# \s espacio
# ' Comillas simples
# " Comillas dobles

'''
re.search(,): busca un patrón en el texto y te dice en donde se encuentra en todo el texto que le pase. 
re.match(,): Hace lo mismo que search pero lo busca al principio del string, no en todos lados digamos.
re.findall(,): devuelve una lista, busca todas las coincidencias para ese patrón.
'''

# Desafío 2
#A: VERDADERO, ya que lo dice el texto
#b será falsa ya que en el texto no hay un inicio de texto
#c: falsa ya que en el texto no se ve un fin de línea
#d: falsa ya que no hay un fin de texto
#Desafío 3
#“X(.*)Y” : Cualquier carácter aparece x cantidad de veces. Busca lo que está entre medio de x e y, busca cualquier substring que tenga en el medio cualquier cosa pero que empiece con X y termine con Y. No importa lo que tenemos entre medio porque me va a traer cualquier cosa que empiece y termine con X e Y. 








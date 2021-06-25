import re
if re.search('patron', 'texto') is not None:
	'bloque de código'
else:
	'bloque de código'

#al buscar no se encuentra nada se devuelve None, el cual es un objeto que nos dice que no hay nada
#De esta manera lo que estamos diciendo es que si la búsqueda no me da un objeto vacío (es decir la búsqueda
#  encontró algo) se ejecuten ciertas órdenes y en caso contrario (si se requiere) se ejecutan otras.

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
re.search(patron, texto).group()
re.search(patron, texto).group(0)
#El método group() (o group(0)) nos devuelve la coincidencia. Sin embargo si lo que se quiere no es encontrar
#  un patrón en particular, sino obtener lo que está dentro de cierto patrón (por ejemplo lo que hay entre ciertas 
# palabras) hay que modificar el patrón.

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*)sit"
re.search(patron, texto).group()
re.search(patron, texto).group(0)
re.search(patron, texto).group(1)
#Acá se utilizaron algunos metacaracteres, como lo son el punto (.) para indicar que puede ser cualquier carácter, y
#  el asterísco (*) para indicar que puede haber 0 o más de estos caracteres. De esta manera obtenemos como resultado
#  lo que se encuentre entre las palabras "ipsum" y "sit", sin embargo observen dos cosas. Primero, el string que nos 
# devuelve tiene dentro un substring que debería haber sido encontrado en la búsqueda: "ipsum dolor sit", pero que sin 
# embargo no aparece. Segundo, nuevamente al hacer group() o group(0) obtenemos la coincidencia, pero si nos queremos 
# quedar con el substring que está contenido entre estas palabras debemos utilizar group(1). Ahora bien, como vimos, usar
#  el patrón de búsqueda de esta manera prioriza los matches externos, es decir, busca el primer delimitador ("ipsum" en
#  nuestro caso) y luego abarca todo hasta la última aparición del segundo delimitador ("sit"). Existe una forma de 
# priorizar los matches internos y es con el metacarácter ?

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
re.search(patron, texto).group()
re.search(patron, texto).group(0)
re.search(patron, texto).group(1)

#Cuando se quieren obtener todas las apariciones del patrón se utiliza el método findall el cual actúa para cada 
# coincidencia como si devolviera el group(1), es decir devuelve en una lista la parte que se encuentra dentro de los 
# delimitadores.

texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = "ipsum(.*?)sit"
re.findall(patron, texto)

#Con las expresiones regulares se puede utilizar un metacarácter \b el cual delimita caracteres alfanúmericos
#  de otros que no lo son. De esta manera podemos obtener las palabras de alguna frase si delimitamos la búsqueda
#  con este metacarácter al inicio y al final. Así podemos, por ejemplo, reemplazar fácilmente alguna palabra en 
# particular.
texto = "Lorem ipsum dolor sit amet, consectetur ipsum elit. Amet sit amet."
patron = r"\bipsum\b"
re.sub('patrón', "lapsus", texto)
re.sub('patrón', "lapsus", texto)
#Lo que hace es sustituir ipsum por lapsus en el texto. 


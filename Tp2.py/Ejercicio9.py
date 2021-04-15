#Hacé un programa que guarde los nombres
#  y la edades de los alumnos de un curso. 
# Se debe introducir el nombre y la edad de 
# cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:
# La edad máxima de todos los alumnos.
# Los alumnos que tengan la edad máxima

lista_nombres = []
lista_edades = []
nombres = input("ingrese nombre:")
if nombres != "*":
    	lista_nombres.append(nombres)
	edad = int(input("ingrese edad:"))
	lista_edades.append(edades)
else:
	print("no hay alumnos")
while nombres != "*":
    nombres = input("ingrese nombre:")
	if nombres != "*":
        lista_nombres.append(nombres)
		edad = int(input("ingrese edad:"))
		lista_edades.append(edades)
    else:
        edad_maxima = max(lista_edades)
		ubicacion = list.findex(lista_edades, edad_maxima)
        nombre_maximo = lista_nombres[ubicacion]

print("la edad maxima es: " + str(edad_max) + "y corresponde a la de" + str(nombre_maximo))
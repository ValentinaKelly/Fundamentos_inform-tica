#Escribí un programa que diga si un string empieza con un número específico.

texto = "1+1 es 2"
primer_caracter = str.find(texto, "1")
if primer_caracter == 0:
    print("Es un numero")
else:
    print("no es un numero")
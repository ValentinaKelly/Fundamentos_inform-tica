#Modificá el programa anterior para que además imprima los caracteres que no aparecen 
# en la cadena, pero con el valor 0.

contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for letra in alfabeto + alfabeto.upper():
	contadores[letra]=0

cadena = input("escribi una cadena:")
for caracter in cadena:
    if caracter.lower() in alfabeto:
		contadores[caracter]+=1
for campo,valor in contadores.items():
    	print (campo,valor)

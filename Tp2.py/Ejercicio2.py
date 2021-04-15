#Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe 
# si es par o impar (el 0 es un número par).

def signo (numero) :
    if abs(numero) == numero:
        print ("es positivo")
    else:
        if numero == 0:
             print ("es cero")
        else:
            print ("es negativo")

print(signo (10))
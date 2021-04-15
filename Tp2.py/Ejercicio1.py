#Crea un programa que lea una cadena por teclado y compruebe si la 
# primera letra es mayúscula o minúscula.

def mayus (cadena):
    if (cadena[0]).isupper() == True:
        print ("la primer letra esmayuscula")
    else:
        print("la primer letra es minuscula")
print(mayus("computadora"))

cadena = str(input("dame una palabra:"))
def es_mayus(palabra):
    if palabra[0] >= "a" and palabra[0] <= "z":
        print("es minuscula")
    else:
        print("es mayuscula")
print(es_mayus(cadena))
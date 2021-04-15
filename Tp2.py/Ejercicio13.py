#Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del 
# otro creando la función esMultiplo.

numero_entero1 = input("ingresar numero entero:")
numero_entero2 = input("ingresar numero entero:")
def multiplo (numero_entero1, numero_entero2):
    return True if numero_entero1 % numero_entero2 == 0 else False

print(multiplo(12, 6))
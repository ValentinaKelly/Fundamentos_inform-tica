#Realizar un programa que lea tres números por 
# teclado y calcule el promedio de ellos.

numero1 = input("ingrese primer numero:")
numero2 = input("ingrese segundo numero:")
numero3 = input("ingrese tercer numero:")
def promedio(numero1,numero2,numero3,cantidad_numeros):
    return((numero1+numero2+numero3)/cantidad_numeros)

print(promedio(4,6,6,3))
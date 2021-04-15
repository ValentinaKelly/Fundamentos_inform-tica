#Pedir el nombre y los dos apellidos de una persona
#  y mostrar las iniciales en mayúsculas
str = input("Ingrese nombre y dos apellidos:")
nombre1 = "susana"
apellido1 = "perez"
apellido2 = "balbi"
if str == "Susana Perez Balbi":
    print(nombre1.capitalize() + apellido1.capitalize() + apellido2.capitalize())
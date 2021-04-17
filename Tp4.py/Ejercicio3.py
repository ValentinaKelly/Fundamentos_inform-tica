#Escribí un programa que lea un archivo, guarde las líneas del archivo en 
# una lista y luego imprima las n últimas.

salida = []
with open("C:\\Users\\LUCAS\\Documents\\Ucema\\Informática\\texto.txt","r") as f:
    lineas = [linea.split() for linea in f]

for linea in lineas:
    print(linea)

with open("C:\\Users\\LUCAS\\Documents\\Ucema\\Informática\\texto.txt","r") as f:
    data = f.readlines()[10]
print(data)
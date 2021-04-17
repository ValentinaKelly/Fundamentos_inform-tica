#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el result"

archivo = open("C:\\Users\\LUCAS\\Documents\\Ucema\\Informática\\texto.txt","r")
lineas = archivo.readlines(70)
print('el archivo tiene', len(lineas), 'lineas')
print('el contenido del archivo')
for linea in lineas:
    print(linea, end='')
archivo.close()

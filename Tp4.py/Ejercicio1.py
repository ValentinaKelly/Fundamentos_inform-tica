#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por 
# ejemplo que imprima cuántas líneas no empiezan con "P").

ocurrencias = []
with open ("C:\\Users\\LUCAS\Documents\\Ucema\\Informática\\texto.txt","r") as lineas:
    for linea in lineas:
        if linea[0] != "P":
            ocurrencias.append(linea)
print(len(ocurrencias))
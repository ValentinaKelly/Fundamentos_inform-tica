#Para abrir un archivo de texto, ya sea para usarlo o escribir en él, podemos usar la función nativa de Python 
#open(): open(path_al_archivo, modo)
#Donde “path_al_archivo” es un objeto de tipo str que indica la ruta en la que se encuentra el archivo, y “modo” es
# un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión. 

#r: abre el archivo solo para leer
#r+ : abre un archivo para lectura y escritura
#a: Abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura
#w: abre un archivo solo para escritura. sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo de escritura. 

#Cierre de archivos: Hay que cerrar los archivos siempre, porque puede eliminarse y no cerrarse automáticamente. 
# Se puede relentizar la máquina por esto. 
#- archivo = open(path_al_archivo, modo)
#- archivo.close()
#- with open(path_al_archivo, modo) as miarch:  Al abrir el archivo de esta forma se guardará automáticamente
#  cuando abajo de esto pongo un código. 

import os
#os.getcwd()      te dice en qué carpeta estás parada

#import glob       permite acceder a todos los archivos que tengo en una ruta, en un directorio
#path = os.getcwd() 
#path
#glob.glob(path+”/*”)      te tira una lista de directorios 
#glob.glob(path+”/*.py”)  Te tira todos los directorios que terminen en .py


#os.chdir(“C:\Users\LUCAS\Documents\Ucema\Informática")  para que te cambie el directorio
#os.getcwd() 
#“C:\Users\LUCAS\Documents\Ucema\Informática"         Y te trae el nuevo directorio

import glob
path = os.getcwd()
print(path)
#Me indica desde el directorio en el que estoy parado en adelante
#Accede a la carpeta que está antes que la que le tiro.

#Desafío
import re
text = open(r"C:\Users\LUCAS\Documents\Ucema\Informática\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt", "r")
abrir_text = open(r"C:\Users\LUCAS\Documents\Ucema\Informática\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt", "r")
texto = abrir_text.read()
print(texto)
print(re.search("-(.*)-",texto))
 
#La escritura de los archivos en Python se hace de forma sencilla con el método write(), que toma como parámetro un string con el contenido que desamos almacenar en el archivo:
#with open(path_al_archivo, modo) as miarch:
    #miarch.write("Este es el contenido del archivo")

#- read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.
#- readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.
#- readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista


#Función input(): input(mensaje) : devuelve en pantalla el mensaje, luego lee lo que se ingresa por el teclado
#  y lo convierte en un string. 
dia = input('Decime que día es hoy:')
#Decime qué día es hoy: Martes
print(dia)
#“Martes”

dia = input('Decime qué número de día es hoy:')
#Decime qué número de día es hoy: 23
print(dia)
#“23”
#Pero día + 2 no funciona ya que se mezclan números enteros con strings

#int(): devuelve el valor entero del objeto que recibe. Siempre utilizo números
int(dia)
#23

dia = int (input ('Decime qué número de día es hoy: '))
#Decime qué número de día es hoy: 23
print(dia)
#23

str(dia)
#“23”

#float(): Siempre utilizo números decimales
float(dia)
#23.0 

print(8/4)
#2.0 

9 // 2  #da el número entero, sin coma
#4

9%2 #Da el resto de la división 
#1 
#Ejercicio 1 Hay que usar len, string e input para hacerlo
string = input( "ingrese una palabra: " )
#ingrese una palabra: Valentina
print(len(string)) #te dice cuántas letras tiene la palabra
#9 

#Ejercicio 2
str = input ('insertar string de minimo 6 letras: ')


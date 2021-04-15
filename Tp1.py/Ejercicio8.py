#Escribir un programa para calcular la nota 
# final de un estudiante, teniendo en cuenta 
# que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta 
# está en blanco no se le suma ni se le resta.

respuesta_correcta = 4
respuesta_incorrecta = -1
sin_respuesta = 0
def nota_final (correctas,incorrectas,sin_respuesta):
    return correctas + incorrectas + sin_respuesta

print(nota_final (4,-2,0))
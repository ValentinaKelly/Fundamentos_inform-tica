#Dada una cierta cantidad de minutos 
# (ingresada por teclado) hacer un programa 
# que muestre cuántas horas y minutos son. Por ejemplo
#  150 minutos son 2 horas y 30 minutos.

tiempo_total = 270
def horas_y_minutos (tiempo_total,minutos):
    return(tiempo_total/minutos)
print(horas_y_minutos(270,60))
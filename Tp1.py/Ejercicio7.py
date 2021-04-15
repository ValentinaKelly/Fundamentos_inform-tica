#Un comerciante, el cual tiene un sueldo base, 
# recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo 
# en cuenta estas ventas y su sueldo base.

def ganancia_final (sueldo,comision):
    return sueldo + (sueldo*comision)

print(ganancia_final(100,0.4))

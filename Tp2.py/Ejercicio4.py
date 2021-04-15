#Una compañía de transporte 
# internacional tiene servicio en algunos 
# países de América del Sur, América Central,
# érica del Norte, Europa y Asia. El costo p
# or el servicio de transporte se basa en el
#  peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:

gramos = int(input("ingrese el peso e gramos:"))
zona = input("ingrese la zona:")
if gramos < 5000:
    if zona == "america del sur":
        print(10 * gramos)
    if zona == "america central":
		print(15 * gramos)
    if zona == "america del norte":
    	print(18 * gramos)
	if zona == "europa":
		print(24 * gramos)
	if zona == "asia":
		print(30 * gramos)
else:
     print("su paquete fue rechazado")
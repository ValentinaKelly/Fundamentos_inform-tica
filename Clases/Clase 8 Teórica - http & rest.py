#nos dará el rtdo de id
#pip install requests en terminal bash
import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
r.json()


#Ejercicio 1 cambiamos el id de 1 a 20, final del url
import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/20')
r.json()

#Ejercicio 2: probar requests.get('https://macowins-server.herokuapp.com/prendas/400')
import requests 
r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
r.json()

r.headers
r.status_code
#Cuando me da como rtdo 200 en lugar de 404 quiere decir que abrió la página y cargó  el contenido. 

#Ejercicio 3: 
import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/')
r.json()

r = requests.get('https://macowins-server.herokuapp.com/ventas/')
r.json()

r = requests.get('https://macowins-server.herokuapp.com/ventas/')
r.json()

#ventas sólo, muestra las ventas totales registradas,
# y ventas/2 sólo muestra la venta que cumple con el id igual a 2

r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon')
r.json()
#trae todos los pantalones que hay, modelos, talles, todo. 

r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=saco')
r.json()
r = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40')
r.json()

#Busco remeras XS:
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
r.json()
#RTA: [{'id': 11, 'tipo': 'remera', 'talle': 'XS'}]

#Ejercicio 4:
#cerebro://recuerdos:3403/recientes#hoy?tema=http
#protocolo:cerebro
#dominio: recuerdos
#puerto: 3403
#ruta: recientes

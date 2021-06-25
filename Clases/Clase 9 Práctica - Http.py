import requests
r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
r.json()
#{'id': 1, 'tipo': 'pantalon', 'talle': 35}
r.json()["id"]
#1
r.json()["tipo"]  #Acá te dice el valor de esa clave
#'pantalon'
r.headers
#{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 'Date': 'Tue, 11 May 2021 16:51:14 GMT', 'Via': '1.1 vegur'}
type(r.headers)
#<class 'requests.structures.CaseInsensitiveDict'>
#r.headers["Content-Type"]
#'application/json; charset=utf-8'
r.headers["Date"]
#'Tue, 11 May 2021 16:51:14 GMT'
r.status_code
#200
#El status_code() me dice si la búsqueda es correcta o no. Si el proceso que le pedí al servidor funcionó ó no. Si me tira 200 es que funciona. 
#Si me da un valor como 404 quiere decir que no lo pudo encontrar.

r = requests.get("https://macowins-server.herokuapp.com/prendas")
r.json()
#[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}, {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, {'id': 17, 'tipo': 'saco', 'talle': 'S'}, {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, {'id': 19, 'tipo': 'saco', 'talle': 'L'}, {'id': 20, 'tipo': 'saco', 'talle': 'XL'}]
#al hacer esto te trae todas las prendas que hay, esto fue porque le saqué el /1 que estaba dsp de prendas
#Prendas/1 me traía únicamente la primer prenda
#Para que nos tire que tenemos de un producto específico hacemos:
r = requests.get("https://macowins-server.herokuapp.com/prendas?tipo=remera")
r.json()
#[{'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}]
#Si quiero agragarle a ver si hay algun talle le agrego &talle=L dsp de remera y me traerá las remeras que hay en ese talle

r = requests.delete("https://macowins-server.herokuapp.com/prendas/21")
r = requests.get("https://macowins-server.herokuapp.com/prendas")
r.json()
#[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}, {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, {'id': 17, 'tipo': 'saco', 'talle': 'S'}, {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, {'id': 19, 'tipo': 'saco', 'talle': 'L'}, {'id': 20, 'tipo': 'saco', 'talle': 'XL'}]
#Lo que hice fue borrar una prenda, por eso al final en el id me dice 20 y no 21
#.get(): te trae la página
#.delete() borra cosas
#.post() lo que hace es agregar un recurso sobre en este caso prendas
#Para agregar información al servidor: data = {"id" : 21}
requests.get("https://macowins-server.herokuapp.com/prendas", data = 'data')
#<Response [200]>
#Acá agregué data a las prendas, te dice que es la rta 200
r = requests.get("https://macowins-server.herokuapp.com/prendas")
r.json()
#[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon', 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}, {'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, {'id': 17, 'tipo': 'saco', 'talle': 'S'}, {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, {'id': 19, 'tipo': 'saco', 'talle': 'L'}, {'id': 20, 'tipo': 'saco', 'talle': 'XL'}, {'id': 'zx8RBAr'}, {'id': '21'}, {'id': 'soy agus'}, {'id': 'hola'}, {'id': '8'}]
#Nos muestra todo lo que fueron agregando en data mis compas


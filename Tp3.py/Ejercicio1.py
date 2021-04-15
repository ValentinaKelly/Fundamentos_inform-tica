#Escribí un programa que verifique si un string tiene al menos un carácter permitido.
#  Estos caracteres son a-z, A-Z y 0-9.

import re
texto = "lorem ipsum dolor sit amet, consectetur adipiscing elit, amet et amet"
patron = "[a-zA-Z0-9]"
def programa_verificado2 (patron,texto):
    if re.search (patron,texto):
        print("verificado")
    else:
        print("no verificado")

print(programa_verificado2(patron,texto))
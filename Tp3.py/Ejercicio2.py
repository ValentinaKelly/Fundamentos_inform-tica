#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. 
# Estos caracteres son a-z, A-Z y 0-9.

import re
def caracteres_permitidos (str):
    return not bool(re.search("[^a-zA-Z0-9]", str))

print("el string", "ABDCEFabdcdef123450", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABDCEFabdcdef123450"))
print("el string", "*&%@#!}{", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("*&%@#!}{"))
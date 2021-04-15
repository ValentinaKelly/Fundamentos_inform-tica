#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

import re
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
def dos_P(lista):
    for elemento in lista:
        resultado = re.match("P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())
dos_P(lista)

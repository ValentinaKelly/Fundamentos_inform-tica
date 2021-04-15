#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
# Recordá que la manera de copiar una lista en otra es:
# lista2 = list(lista1)

lista = [ ]
for a in range(5):
    lista.append(input("Dame un elemento:"))

lista_2 = list(lista)
lista_2.reverse()
print(lista_2)

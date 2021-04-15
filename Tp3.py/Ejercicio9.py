#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

texto = input("ingrese comida favorita:")
comida_favorita = texto.split('_')
print(comida_favorita)

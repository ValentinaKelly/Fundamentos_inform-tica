#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

texto = '   programacion con _python  '
texto = texto.replace(' ', '|')
texto_corregido = texto.replace('_', '|')
print(texto_corregido)
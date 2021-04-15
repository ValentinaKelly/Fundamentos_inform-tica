#Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de dos o tres e.

import re
def encontrar_patron(string):
    patron = "he+"
	if re.search(patron, string) is not None:
		    return "se encontró el patron"
	else:
		    return "no se encontró el patron"
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeeeee"))

def encontrar_patron(string):
    patron = "he{2,3}"
	if re.search(patron,string) is not None:
		    return "se encontro el patron"
	else:
		    return "no se encontro el patron"
print(encontrar_patron("he"))
print(encontrar_patron("heeeey"))


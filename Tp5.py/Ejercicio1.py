#Dada la siguiente clase, identificá la interfaz y el estado de la misma:
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
#Los mensajes que entienden y a los que responde es una interfaz. Y el estado de los objetos vendrían a ser como la “energía” 
# que tenían los objetos. 
# Puede ser modificado mediante mensajes. 
# Estado: atributos que tiene un objeto, interfaz: métodos del objeto y mensajes que entiende. 
#Viendo esta clase podemos darnos cuenta que la interfaz energía, comer, acariciar, esta debil. Y el estado sería alimento y caricias. 

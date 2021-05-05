#Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible 
# indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
#inc()
#dis()
#reset()
#valorActual()
#valorNuevo(nuevoValor)
#Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

class Contador:
    def _init_(self, valor = 0):
        self.valor = valor
        self.valor_inicial = valor
    def inc(self):
        self.valor += 1
    def dis(self):
        self.valor -= 1
    def reset(self):
        self.valor = 0
    def valorActual(self):
        print(self.valor)
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor    

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()                    
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
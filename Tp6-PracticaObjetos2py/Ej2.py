class Dispositivo:
    def cargar_a_tope(self):
        self.bateria = 100
    
    def descargado(self):

class Celular(Dispositivo):
    def _init_(self):
        self.bateria = 100
    
    def utilizar(self, min):
        self.bateria -= min/2

class Notebook(Dispositivo):
    def _init_(self):
        self.bateria = 100
    def utilizar(self, min):
        self.bateria -= min

class CArgadorUniversal:
    def _init_(self):
        self.dispositivos = []
    def agregar(self,dispositivo):
        self.dispositivos.append(dispositivo)
    def cargar(self):
        for i in self.dispositivos:
            i.cargar_a_tope()

un_celu = Celular()
una_notebook = Notebook()
un_celu.descargado()
un_celu.utilizar(100)
un_celu.descargado()
una_notebook.utilizar(100)
una_notebook.cargar_a_tope()
una_notebook.descargado()

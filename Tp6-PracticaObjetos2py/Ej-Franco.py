class Dispositivo:
    def cargar(self):
        self.bateria = 100
    def descargado(self):
        self.bateria <= 20
    def valor_bateria(self):
        self.bateria = 100
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
class CargadorUniversal:
    def _init_(self):
        self.dispositivos = []
    def agregar(self, dispositivo):
        self.dispositivos.append(dispositivo)
    def cargar(self):
        for i in self.dispositivos:
            i.cargar()

un_celular = Celular()
una_notebook = Notebook()
un_celular.descargado()
un_celular.utilizar(180)
un_celular.descargado()
una_noebook.utilizar(100)
una_notebook.cargar()
una_notebook.descargado()



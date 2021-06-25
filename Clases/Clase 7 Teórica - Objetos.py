#Hace a hipo, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y hacerlos entrenar todos los dias, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)
#Para crear a Hipo tenemos que arrancar creando la clase de entrenadores de dragones, y a partir de ahí crear a Hipo.
class EntrenadorDeDragones():
	def _init_(self, vacantes, alumnos):
		self.vacantes = vacantes
		self.dragones_aceptados = alumnos

		
def aceptar_dragon(self,ave):
	if self.vacantes - 1 > 0:
		self.dragones_aceptados.appen(ave)
		self.vacantes -= 1

#Hacé que hipo pueda entrenar a las golondrinas. ¿Qué comportamiento deberían entender las golondrinas ahora?
class EntrenadorDeAves():
    def __init__(self, vacantes):
        self.vacantes = vacantes
        self.alumnos_aceptados = []
    def aceptar(self, alumno):
        if self.vacantes > 0:
            self.alumnos_aceptados.append(alumno)
            self.vacantes -= 1
    def entrenar(self):
        for alumno in self.alumnos_aceptados:
            for _ in range(0, 20):
                alumno.volar_en_circulos()
            alumno.saciar()

#Por panamericana: Ah, pero no tan rápido. Ahora te toca a vos: implementá el método volar_por_panamericana que nos permite decirle a un animal alado que vuele hasta un cierto lugar a lo largo de ciudades de la Ruta Panamericana. Tené en cuenta algunos puntos notables de la ruta:
#Ushuaia es el km 0
#Buenos Aires es el km 3078
#Valparaiso (Chile) es el km 4533
#Bahía Prudhoe (Alaska) es el km 17958.
#Para pensar: ¿tiene algo raro este nuevo método?

def arranca_en(self, ciudad):
    self.ciudad_actual = ciudad
def volar_por_panamericana(self, ciudad_destino):
    kms = abs(self.ciudad_actual - ciudad_destino)
    self.volar(kms)
    self.ciudad_actual = ciudad_destino

valparaiso = 4533
buenos_aires = 3078
ushuaia = 0
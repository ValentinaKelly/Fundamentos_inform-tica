class Golondrina:
 def __init__(self, energia):
   self.energia = energia
 
 def comer_alpiste(self, gramos):   # (qué va hacer, se denomina método pero no es una función,   ya que se invocan como 
                                           #función(argumentos), y los métodos lo hacen comoenvío de mensaje: objeto.mensaje(argumento))
                                                                    #Van siempre dentro de una clase. 
   self.energia += 4 * gramos             #(cómo lo va a hacer)
 
 def volar_en_circulos(self):
   self.volar(0)
 
 def volar(self, kms):
   self.energia -= 10 + kms
 
class Dragon:    
    def __init__(self, cantidad_dientes, energia):
        self.energia = energia
        self.cantidad_dientes = cantidad_dientes
 
    def escupir_fuego(self):
        self.energia -= 2 * self.cantidad_dientes
 
    def comer_peces(self, unidades):
        self.energia += 100 * unidades
 
    def volar_en_circulos(self):
        self.energia -= 1
 
    def volar(self, kms):
         self.energia -= 10 + kms/10
 
pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
 

#Los objetos vienen a partir de clase, ya que todo objeto es un ejemplo de la clase. Pepita y Anastasia son 
# objetos de la clase Golondrina. Pepita sería una instancia de golondrina. Las clases son siempre en singular, 
# por eso golondrina y no golondrinas. 

#from aves import Golondrina
maria = Golondrina(42)
maria.energia
maria.volar_en_circulos()  #entendemos que maría sabe volar ya que así están configuradas las golondrinas. 

# 1)Programa que te diga si pepita está débil
def esta_debil(self):
    if self.energia <= 10:
        return True
    else: 
        return False 

#si hago:
maria.energia <= 10
#me dará tmb True o False

#Está feliz si tiene más de 500ptos.
def esta_feliz(self):
    if self.energia >= 500:
        return True
    else:
        return False


#from aves import *   #(nos importa todo lo q hay en aves)


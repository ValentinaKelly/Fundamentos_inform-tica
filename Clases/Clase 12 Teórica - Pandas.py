import pandas as pd
import seaborn as sns
import sklearn 
import matplotlib.pyplot as plt


iris = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Informática\iris_data.txt", sep = '\t')
print(iris)
# El tipo de datos es 'num', hay 3 tipos de especies y 4 características para cada uno (largo
#  y ancho del pétalo, largo y ancho del sépalo. El sépalo la parte de abajo de la flor).
iris.info() #Acá me hace un resumen de las columnas, los datos no nulos y el tipo. 
iris.describe()#Datos estadísticos
#Si quiero calcular la mediana del sepal.lenght
#iris['sepal.lenght'].median()
#Si quiero onocer la frecuencia de los datos gráficamente:
g = sns.histplot(data = iris, x = "petal.length", binwidth=0.25, kde = True)
plt.show() #Lo que vemos gráficamente es que está la forma de campana pero hay dos dtos mayores que la quiebran
#Estamos contando cuántas veces aparece cada registro, su frecuencia en base a los valores
#El valor en medio de estos será la mediana
#Vemos que hay conjuntos separados de datos en el petal.lenght 
#Para graficar todo junto:
v = sns.pairplot(iris)
plt.show() #Nos muestra gráfico de barras y gráfico de disperción, relaciona dos variables
# Mezcla de a dos variables por lo tanto en uno hay sepal.lenght y petal.width y así
#Cuando es la misma variable en ambos ejes nos pone un gráfico de barras
# En los espacios donde no hay nada, podemos pensar que podríamos separar las plantas en dos grupos
# debido a que hay características que no coinciden para ninguno de las variables, y características que
# coinciden para ambas. Da un indicio de criterios para separar. 





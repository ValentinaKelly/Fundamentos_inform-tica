import pandas as pd
from scipy.sparse import data
import seaborn as sns
import sklearn 
import matplotlib.pyplot as plt
from sklearn import datasets #sklearn es LA biblioteca de machine learning de python
from sklearn.cluster import KMeans, DBSCAN #Para usar kmeans
from sklearn.preprocessing import StandardScaler #Para estandarizar nuestros datos
from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
from sklearn.cluster import AgglomerativeClustering #Para clustering jerárquico
from sklearn.metrics import pairwise_distances #Para las distancias a pares

iris = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Informática\iris_data.txt", sep = '\t')

# Estas operaciones pueden hacerse muy fácilmente con la clase StandardScaler, del módulo scikitlearn:
scaler = StandardScaler()
iris_escaleado = scaler.fit_transform(iris)

k = 3  #definimos la cantidad de clusters (grupos)
kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones
# Siendo el máximo numer de iteraciones que vamos a hacer. Sería la cant de veces que vuelve a calcular todo.
# Random state es un cálculo interno para poder sacar los centroides, es un nro al azar
kmeans.fit(iris_escaleado)  #aplicamos el método a nuestros datos
#la asignación de cada punto a un cluster se obtiene de la propiedad labels_ del objeto clusters.
kmeans.labels_ #Vemos a que valor le adjudica cada etiqueta
kmeans.cluster_centers_ #Los centroides pueden ser obtenidos con cluster_centers_:

#Para entender mejor los resultados obtenidos grafiquemos la distribución de puntos, pintando cada punto según el color
#  correspondiente al etiquetado:

colores = ['red', 'green', 'blue']
g = sns.scatterplot(x=iris_escaleado[:,2], y=iris_escaleado[:,3], hue=kmeans.labels_, palette=colores, alpha=0.5)
g = sns.scatterplot(x=kmeans.cluster_centers_[:,2], y=kmeans.cluster_centers_[:,3], zorder= 10, palette=colores, hue=[0, 1, 2], legend=False, markers=6, s=200)
#plt.show()
#hue me permite ordenar los datos en base a tales datos
#Cuanto mas veces iteras los datos más específicos serán los datos
#Seaborn.pydata.org tiene formas de hacer los gráficos

#Desafio 6: Calculá la inercia para distintos valores de k y almacenalos en un DataFrame
inertias_dict={}
inertias_dict["K"]=[]
inertias_dict["Inertia"]=[]
for i in range(15):
  k = i + 1
  kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
  kmeans.fit(iris_escaleado)
  inertias_dict["K"].append(k)
  inertias_dict["Inertia"].append(kmeans.inertia_)
print(inertias_dict)

inertias_df=pd.DataFrame(inertias_dict)
inertias_df

#Desafío 7:Realizá un gráfico de inercia vs k, usando el método pointplot de seaborn
sns.pointplot(data=inertias_df,x="K",y="Inertia")
#plt.show()


#Lo que quiero ver es la incercia de los valores k, por lo tanto no quiero ni algo q sea muy alto que se diferencie
# mucho, ni una inercia muy baja que varíe del resto. Elegiría una K donde el aumento de su valor no disminuye ni aumenta
# mucho la inercia. En el codo del gráfico serán los mejores valores de k a elegir. 2, 3, 4. 

from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
#Calculamos el promedio del silhouette de todos
silhouette_avg = silhouette_score(iris_escaleado, kmeans.labels_)
#Calculamos el silhouette de cada punto
sample_silhouette_values = silhouette_samples(iris_escaleado, kmeans.labels_)

#si ejecutamos esto es calcular otro valor, silhouette, el valor de cohesión. Tiene en cuenta todos los puntos en relación
# al centroide. 

import matplotlib.pyplot as plt #Para graficar
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm #Para graficar el silhouette
import numpy as np
def graficarSilhouette (k, labels, sample_silhouette_values, silhouette_avg):
    fig, ax1 = plt.subplots(1, 1)
    y_lower = 10
    for i in range(k):
      ith_cluster_silhouette_values = \
          sample_silhouette_values[labels == i]

      ith_cluster_silhouette_values.sort()

      size_cluster_i = ith_cluster_silhouette_values.shape[0]
      y_upper = y_lower + size_cluster_i

      color = cm.nipy_spectral(float(i) / k)
      ax1.fill_betweenx(np.arange(y_lower, y_upper),
                        0, ith_cluster_silhouette_values,
                        facecolor=color, edgecolor=color, alpha=0.7)
      ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
      y_lower = y_upper + 10
    ax1.set_title("Plot del silhouette de cada cluster")
    ax1.set_xlabel("Coeficiente de silhouette")
    ax1.set_ylabel("Etiqueta del cluster")
    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax1.set_yticks([])

graficarSilhouette (k, kmeans.labels_, sample_silhouette_values, silhouette_avg)
#Desafío 9: Calculá la silhouette para distintos valores de k, desde 2 a 10, y almacenalos en un DataFrame
#Barramos un rango de k posible y veamos el mejor k
silhouette_avg = [] #generamos una lista vacía
for k in range (2, 11): #probamos desde 2 clusters hasta 10, silhoutte no se puede calcular para un solo cluster
    kmeans = KMeans (n_clusters=k, init='random', n_init=10, max_iter=300, random_state=1234457)
    kmeans.fit(iris_escaleado)
    silhouette_avg.append(silhouette_score(iris_escaleado, kmeans.labels_))

#Desafío 10: Realizá un gráfico de inercia vs k, usando el método pointplot de seaborn
df = pd.DataFrame({'K': list(range(2, 11)), 'SilhouettePromedio': silhouette_avg})
g = sns.pointplot(data=df, x='K', y='SilhouettePromedio')
plt.show()

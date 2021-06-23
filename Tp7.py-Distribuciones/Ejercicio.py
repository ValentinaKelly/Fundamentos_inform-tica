
# %matplotlib inline
import pandas as pd #Pandas para usar dataframes
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm #Para graficar el silhouette
import seaborn as sns #Para graficar
import numpy as np #Para realizar operaciones númericas con matrices y arrays
from sklearn import datasets #sklearn es LA biblioteca de machine learning de python
from sklearn.cluster import KMeans, DBSCAN #Para usar kmeans
from sklearn.preprocessing import StandardScaler #Para estandarizar nuestros datos
from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
from sklearn.cluster import AgglomerativeClustering #Para clustering jerárquico
from sklearn.metrics import pairwise_distances #Para las distancias a pares
from scipy.cluster.hierarchy import dendrogram, cophenet, linkage #Para graficar los dendrogramas y calcular el coeficiente cofenetico
from scipy.cluster import hierarchy #Para graficar los dendrogramas
from scipy.spatial.distance import pdist #Para calcular la distancia con el coeficiente cofenetico
'''TP 7'''
#Paso 1: cargar los datos
stock_data = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\dataset_clustering_teorico.csv")

#Paso 1 Inspeccioná el DataFrame y caracterizalo
'''stock_data.info() #Para ver qué tipo de datos tengo
stock_data.describe() #Para obtener los datos estadísticos
#Primeramente podemos ver que hay una gran diferencia entre el promedio, el mínimo y máximo. Tenemos que normalizar los valores para que se encuentren
# dentro del mismo rango. '''
stock_data1 = stock_data.drop('Unnamed: 0',axis=1) #eliminé su primera columna ya que para hacer clustering debo tener únicamente datos numéricos

#Paso 2 Normaliza los datos y guardálos en una variable llamada stock_data_normalizado
'''stock_data1_norm = (stock_data1-stock_data1.min())/(stock_data1.max()-stock_data1.min())'''
#Con esto lo que hago es que el valor mínimo sea cero y el valor máximo sea 1, para que se encuentren en un mismo rango
scaler = StandardScaler()
stock_data1_norm = scaler.fit_transform(stock_data1)

#Paso 3 Aplicá el método k-means usando k=14
k = 14  #definimos la cantidad de clusters
kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457) #tomamos los centroides de forma aleatoria y definimos un máximo de 300 iteraciones
kmeans.fit(stock_data1_norm)  #aplicamos el método a nuestros datos
kmeans.labels_
kmeans.cluster_centers_ 
colores = ["red", "green", "blue"]
g = sns.scatterplot(x = stock_data1_norm[:,2], y = stock_data1_norm[:, 3], hue = kmeans.labels_, palette = colores, alpha = 0.5)
g = sns.scatterplot(x = kmeans.cluster_centers_[:,2], y = kmeans.cluster_centers_[:,3], zorder = 10, palette = colores, hue = [0, 1, 2], legend = False, markers=6, s=200)
plt.show() 
#Paso 4 Evaluá tus resultados
inertias_dict={}
inertias_dict["K"]=[]
inertias_dict["Inertia"]=[]
for i in range(15):
  k = i + 1
  kmeans = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
  kmeans.fit(stock_data1_norm)
  inertias_dict["K"].append(k)
  inertias_dict["Inertia"].append(kmeans.inertia_)
print(inertias_dict)

inertias_df=pd.DataFrame(inertias_dict)
inertias_df

from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
#Calculamos el promedio del silhouette de todos
silhouette_avg = silhouette_score(stock_data1_norm, kmeans.labels_)
#Calculamos el silhouette de cada punto
sample_silhouette_values = silhouette_samples(stock_data1_norm, kmeans.labels_)

#si ejecutamos esto es calcular otro valor, silhouette, el valor de cohesión. Tiene en cuenta todos los puntos en relación
# al centroide. 

import matplotlib.pyplot as plt #Para graficar
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm #Para graficar el silhouette
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



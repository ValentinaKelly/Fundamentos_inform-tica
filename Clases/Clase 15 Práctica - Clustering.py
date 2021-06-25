
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
stock_data.head()

#Paso 1 Inspeccioná el DataFrame y caracterizalo
stock_data.describe() #''Podemos ver que la media y la mediana son muy similares, por lo que podría llegar a ser una distribución normal'''
stock_data.plot.hist(); #Gráficamente podría llegar a ser una distribución normal
#plt.show()


#Paso 2 Normaliza los datos y guardálos en una variable llamada stock_data_normalizado
scaler = StandardScaler()
stock_data_normalizado = scaler.fit_transform(stock_data)
print(str(stock_data_normalizado))
#Paso 3 Aplicá el método k-means usando k=14
#Paso 4 Evaluá tus resultados


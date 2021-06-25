import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
datos = pd.read_csv(r'C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\Datos.csv')
datos.head()
datos.info()
datos_filtrados = datos.dropna() #Sacamos todos los NaN

datos2 = datos_filtrados[datos_filtrados['Altura']<2.3] #Así sacamos los datos de altura que son ilógicos para la altura
# de personas, nos dará únicamente los datos con alturas menores a 2.3
print(datos2.plot.scatter('Nombres', 'Sueldo')) #ACá vemos gráficamente que hay uno que cobra mucho más q el resto
# Por lo tanto lo descartamos porq no es parámetro para nosotros
datos3 = datos2[datos2['Sueldo']<200000] #Queremos los sueldos menores a los que no son parámetros
datos3['Sueldo'].mode() #Nos da la moda de los sueldos
g = sns.histplot(data=datos3, x='Sueldo', binwidth=0.25, kde=True)
print(g)





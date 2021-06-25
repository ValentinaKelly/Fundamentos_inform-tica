import pandas as pd
import seaborn as sns
import scipy.stats as ss


#Podemos cargar (leer) la el contenido del archivo en un DataFrame de Pandas:
personas =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\personas_2011.csv",sep=';')
personas.head()
#Al imprimir el DataFrame se ven celdas con valores NaN ¿Qué son esos valores?¿Qué significa? ¿A qué columna corresponden estos valores? 
#¿Qué tipo de datos son los pertenecientas a cada una de las columnas (categóricos o numéricos)?
#Los NaN quieren decir is not a number, y aparecen en datos que se desconocen o no pueden ser compartidos por equis motivo. Corresponden a Non-Null Count; Dado que tenemos 
# una línea de base de cuántos valores dentro de una columna deben tener valores no nulos para que podamos usarlos para el análisis, pero no podríamos eliminar todos esos datos porque 
# son todas las columnas
personas.info() #Para obtener la información general del DataFrame
#esta es una descripción genérica de nuestro DataFrame, de la cuál podemos obtener el nombre de cada columna (variable), el tipo de datos correspondiente
# a cada una de ellas, y cuántas filas por columna poseen información.
personas.describe() #análisis estadístico básico de nuestro conjunto de datos
#promedio de edades es de 38 años
#un promedio no tiene sentido alguno para esta variable
#podemos calcular la frecuencia de aparición de cada una de estas categorías/datos. 
# Esto es contar cuántas veces del total de filas aparece cada una de ellas:
personas['maximo_grado_academico_id'].value_counts()

#Desafío I: Tomando las tablas de referencia del MinCyT y tomando lo aprendido en el recorrido anterior, incorporá los 
# datos correspondientes a todas las variables categóricas de la tabla
clase_cargo =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_clase_cargo.csv",sep=';')
disciplina =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_disciplina.csv",sep=';')
grado_academico =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_grado_academico.csv",sep=';')
sexo =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_sexo.csv",sep=';')
condicion_docente=  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_tipo_condicion_docente.csv",sep=';')
dedicacion_horaria_semanal =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_tipo_dedicacion_horaria_semanal.csv",sep=';')
tipo_personal =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_tipo_personal.csv",sep=';')

personas_corregido = pd.merge(personas, clase_cargo,  on='categoria_conicet_id')
personas_corregido.to_csv('personas_completas.csv', index=False, na_rep='Unknown')
print(personas_corregido)

print(personas.isnull().sum()) #cuantificar cuántas celdas hayen nuetsra tabla sin información.

import matplotlib.pyplot as plt
sns.heatmap(personas.isnull(), cmap='viridis')
plt.show()
#La función ISNULL() devuelve un valor especificado si la expresión es NULL. Si la expresión es NOT NULL, esta función devuelve la expresión.

#Desafío II: Calcular el porcentaje del total de datos, representan los datos nulos de cada columna (variable)
len(personas_corregido)/personas.isnull().sum() *100


import pandas as pd
import seaborn as sns
import scipy.stats as ss

#Creo un DataFrame vacío haciendo:
variable = pd.DataFrame()
#Si imprimo esto me muestra que no tiene nada dentro
#Para crear un DataFrame y pasarle las columnas:
variable = pd.DataFrame(columns=['columna1', 'columna2'])
#Para crear un Data Frame a partir de un diccionario:
variable = {'clave':['valor1', 'valor2'], 'clave2': ['valor1', 'valor2']}
df = pd.DataFrame(variable) #Ahí crea el DataFRame a partir del dicc
#Para que el data frame funcione como diccionario debe haber siempre la misma cantidad
#de elementos entre las claves y los valores de todo el dic. 

'''df es el nombre genérico que se usa para identificar un data frame.'''

#Desafío I: Estos métodos aceptan otros parámetros que merecen la pena ser explorados. Averiguá para qué sirven los parámetro sep, index_col, nrows y header
# ,sep=';' #Esto lo que hace en arreglar los textos cuando te los dan de diferente manera que en columnas y filas
# df.head() #Imprime las primeras 5 rows del data frame. Si le paso el valor de filas entre paréntesis me las trae tmb
# df.tail() #Me imprime las últimas 5 filas del df
# df.info(): te devuelve nombre de las columnas en forma de listas, con el conteo de datos que no son nulos
# y te dice que tipo de dato tiene.
# index_col ordena en primer lugar la columna correspondiente al número que le pases, si index_col = 0 la tabla se ordena norma
# nrows te devuelve las primeras filas corrspondientes al numero que le pasas, si le pones = 0 te resume la tabla
# df.describe() te da datos estadísticos: count, mean, std, min, max, y porcentajes
df = pd.read_csv(r'path', sep = ';', index_col = 0, nrows = 0, headers = 68551)
#nos da la info de ese dato 68551

#Desafío II: Descargá a tu computadora la tabla de personas que conforman el Ministerio de Ciencia y Tecnología de Argentina, en formato csv.
df = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\personas_2011.csv",sep=';')

#Desafío IV: Extrae la columna seniority_level y contá cuántas personas tenían expertice nivel B, C y D
print(df["seniority_level"]) #es un objeto
df.groupby('seniority_level')[['persona_id']].count()
# B=6674 C=13645 D=5774

#Desafío V: ¿Qué resultados obtuviste en cada caso? Explicá qué hace cada linea de código
df['seniority_level'].value_counts() #no te toma si no le agregas un print
df["seniority_level"].count() #Cuántos hay en la columna seniority level
df.groupby("seniority_level").count() #Cuenta todos los datos que corresponden a cada categoría de Seniority level de acuerdo a cada columna
df.groupby("seniority_level")[["persona_id"]].count() #Para ver los datos enumerados de la columna id. 
#Cuenta cuántos datos de la columna persona id pertenecen a las categorías de Seniority

df['edad'] * 2
df['edad'] + 2
df['edad'] > 2  
df[df['edad'] > 35 ]

#Desafío V: Contá cuántas personas de 30 años ingresaron al ministerio en 2011 ¿Cuántas formas de hacer este cálculo se te ocurr
anio2011=df[df["anio"]==2011]
anio2011[anio2011['edad']==30]
#Para obtener la edad también puedo hacer:
df.loc[2, 'edad']

#Para obtener los datos de una columna como lista:
#tolist()
df['columna'].tolist()

#Descargala en formato csv y cargala en un nuevo DataFrame de nombre df_cat 🧗‍♀️ Desafío VII: Identificá si existen columnas en común con el DataFrame grande
path = r'C:\Users\LUCAS\Documents\Ucema\Programación\ref_categoria_conicet.csv'
df_cat = pd.read_csv(path, sep=';')
list(df) == list(df_cat)
#Nos tira False en la terminal
columnas_en_comun = []
for columna in list(df):
    if columna in list(df_cat):
        columnas_en_comun.append(columna)
print(columnas_en_comun)


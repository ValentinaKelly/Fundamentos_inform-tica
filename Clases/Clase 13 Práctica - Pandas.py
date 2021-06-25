#Creá un nuevo DataFrame a partir del DataFrame Personas, el cual solo tenga las columnas "persona_id", "anio" y "categoria_conicet_id" (guardalo en una variable llamada pers)
from typing import ClassVar
import pandas as pd
from pandas.core.frame import DataFrame
import seaborn as sns
import scipy.stats as ss


pers = pd.DataFrame({'personas_id':[], 'anio':[], 'categoria_conicet_id':[]})
conicet = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_categoria_conicet.csv",sep=';')

clase_cargo =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_clase_cargo.csv",sep=';')
disciplina =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_disciplina.csv",sep=';')
grado_academico =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_grado_academico.csv",sep=';')
sexo =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_sexo.csv",sep=';')
condicion_docente=  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_tipo_condicion_docente.csv",sep=';')
dedicacion_horaria_semanal =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_tipo_dedicacion_horaria_semanal.csv",sep=';')
tipo_personal =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_tipo_personal.csv",sep=';')
personas =  pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\personas_2011.csv",sep=';')
categoria = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_categoria_conicet.csv",sep=';')


completo = [personas, categoria, clase_cargo, disciplina, grado_academico, sexo, condicion_docente, dedicacion_horaria_semanal, tipo_personal]
conicet = pd.read_csv(r"C:\Users\LUCAS\Documents\Ucema\Programación\Bases de datos\ref_categoria_conicet.csv",sep=';')

pers = pd.concat([personas['persona_id'], personas['anio'], personas['categoria_conicet_id']], axis = 1)
pd.merge(pers, conicet, how='right', on='categoria_conicet_id')
pd.merge(pers, conicet,how="left", on = "categoria_conicet_id")
pd.merge(pers, conicet,how="outer", on = "categoria_conicet_id")
pd.merge(pers, conicet,how="inner", on = "categoria_conicet_id")
pd.merge(pers, conicet, left_on= 'persona_id', right_on = 'categoria_conicet_id')

#Creá un DataFrame pers2 que contenga las columnas de pers excepto la columna "categoria_conicet_id" y luego probá hacer:
pers2 = pd.concat([personas['persona_id'], personas['anio']])
pd.merge(pers2, conicet,how = "inner", left_on="persona_id", right_on = "categoria_conicet_descripcion")

#Obtener las 10 personas con mayor edad y generar un nuevo DataFrame con la información de el id de la persona, el año, su edad
#  y las producciones académicas de los últimos 4 años. Unirlo con el DataFrame conicet y en base a ese generar una tabla con el id de la
#  persona y la descripción de la categoría en conicet. Luego guardar este último DataFrame en un archivo.

print(completo.max.head(10))

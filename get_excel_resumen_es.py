import pandas as pd

#lee el archivo csv 
df_educ_sup=pd.read_csv("20230714_Titulados_Ed_Superior_2022_WEB.csv",sep=";",header=0)

df_educ_sup=df_educ_sup[df_educ_sup["nivel_carrera_2"]=="carreras Profesionales"]

#df_count_carreras=df_educ_sup.groupby('nomb_titulo_obtenido')#.reset_index(name='Conteo')

print(df_educ_sup)
df_educ_sup.to_excel("carreras.xlsx")
#df_count_carreras.to_excel("resumen_educacion_superor.xlsx",index=false,sheet_name='res_carr')



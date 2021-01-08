##Temp class in case we need to perform same operation on other files.
# Can be deleted later on.
# Note that DF's and JSON's are data objects and must be treated likewise.

import pandas as pd

df_listasSwadesh = pd.read_excel("..\..\Resources\Listas Swadesh.xlsx", sheet_name="Hoja1")
# df_vocales.to_json(r'C:\Users\luses\Documents\U\UCR\Asistencia\Metricas\linguistica\vocales.json')
# df_consonantes.to_json(r'C:\Users\luses\Documents\U\UCR\Asistencia\Metricas\linguistica\consonantes.json')
print(df_listasSwadesh)
df_listasSwadesh.to_json(r'C:\Users\luses\Documents\U\UCR\Asistencia\Metricas\linguistica\listasSwadesh.json')



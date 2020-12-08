# from pandas import read_excel

# Run the following
from chibcha import *
M = languageMatrix()
language_list = list(chibchan_swadesh_lists.keys())
nM, nN = branchingStep(M,language_list)


# df_listas = read_excel("../../Resources/ListasSwadesh.xlsx", sheet_name="Hoja1")

# df_vocales.to_json(r'C:\Users\luses\Documents\U\UCR\Asistencia\Metricas\linguistica\vocales.json')

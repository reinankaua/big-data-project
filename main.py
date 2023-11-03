import pandas as pd
import numpy as np

df = pd.read_excel("dados.xlsx", sheet_name="Vítimas")

# for index, row in df.iterrows():
#     if row['UF'] == ("Amazonas" or "Pará" or "Roraima" or "Amapá" or "Rondônia" or "Acre" or "Tocantins"):
#         df.loc[index, 'Região'] = "Norte"

df_homicidios = df[df['Tipo Crime'] == 'Homicídio doloso']

# def setRegiao(uf):
#     if uf == "Amazonas" or "Pará" or "Roraima" or "Amapá" or "Rondônia" or "Acre" or "Tocantins":
#         return "Norte"
#     else:
#         return 'OK'
# energi teleco
#
# df_homicidios['Região'] = df_homicidios['UF'].map(setRegiao)
#

print(df_homicidios)

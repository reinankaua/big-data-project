import pandas as pd
import numpy as np

df = pd.read_excel("dados.xlsx", sheet_name="Vítimas")
#
# for index, row in df.iterrows():
#
#     if row['UF'] == ("Amazonas" or "Pará" or "Roraima" or "Amapá" or "Rondônia" or "Acre" or "Tocantins"):
#         df.loc[index, 'Região'] = "Norte"

for index, row in df.iterrows():
    match row['UF']:
        case 1:
             "Domingo"
        case 2:
             "Segunda-Feira"
        case 3:
             "Terça-Feira"
        case 4:
             "Quarta-Feira"
        case 5:
             "Quinta-Feira"
        case 6:
             "Sexta-Feira"
        case 7:
             "Sábado"
        case _:
             "NaN"

df_homicidios = df[df['Tipo Crime'] == 'Homicídio doloso']

# def setRegiao(uf):
#     if uf == "Amazonas" or "Pará" or "Roraima" or "Amapá" or "Rondônia" or "Acre" or "Tocantins":
#          "Norte"
#     else:
#          'OK'
# energi teleco
#
# df_homicidios['Região'] = df_homicidios['UF'].map(setRegiao)
#

print(df_homicidios)

import datetime
import dateparser
import pandas as pd

df = pd.read_excel("dados.xlsx", sheet_name="Vítimas")

estados_norte = ["Amazonas", "Pará", "Roraima", "Amapá", "Rondônia", "Acre", "Tocantins"]
estados_nordeste = ["Piauí", "Maranhão", "Pernambuco", "Rio Grande do Norte", "Paraíba", "Ceará", "Bahia", "Alagoas", "Sergipe"]
estados_centro_oeste = ["Mato Grosso", "Mato Grosso do Sul", "Goiás", "Distrito Federal"]
estados_sudeste = ["São Paulo", "Rio de Janeiro", "Espírito Santo", "Minas Gerais"]
estados_sul = ["Rio Grande do Sul", "Paraná", "Santa Catarina"]

for index, row in df.iterrows():
    if row['UF'] in estados_norte:
        df.loc[index, 'Região'] = "Norte"
    elif row['UF'] in estados_nordeste:
        df.loc[index, 'Região'] = "Nordeste"
    elif row['UF'] in estados_centro_oeste:
        df.loc[index, 'Região'] = "Centro Oeste"
    elif row['UF'] in estados_sudeste:
        df.loc[index, 'Região'] = "Sudeste"
    elif row['UF'] in estados_sul:
        df.loc[index, 'Região'] = "Sul"

    else:
        df.loc[index, 'Região'] = "NaN"

def converter_mes_para_numero(mes):
  return dateparser.parse(mes, languages=['pt']).month

# df['mes_numerico'] = df['Mês'].apply(lambda mes: datetime.datetime.strptime(mes, '%b').month)
df['mes_numerico'] = df['Mês'].apply(converter_mes_para_numero)
df['data_completa'] = df['mes_numerico'].astype('str') + '-' + df['Ano'].astype('str')

df_homicidios = df[df['Tipo Crime'] == 'Homicídio doloso']

print(df_homicidios)
df_homicidios.to_excel('dados-tratados.xlsx')
print('Planilha crianda com sucesso.')


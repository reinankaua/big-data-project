import pandas as pd

df = pd.read_excel("dados.xlsx", sheet_name="Vítimas")

for index, row in df.iterrows():
    match row['UF']:
        case "Amazonas":
            df.loc[index, 'Região'] = "Norte"
        case "Pará":
            df.loc[index, 'Região'] = "Norte"
        case "Roraima":
            df.loc[index, 'Região'] = "Norte"
        case "Amapá":
            df.loc[index, 'Região'] = "Norte"
        case "Rondônia":
            df.loc[index, 'Região'] = "Norte"
        case "Acre":
            df.loc[index, 'Região'] = "Norte"
        case "Tocantins":
            df.loc[index, 'Região'] = "Norte"

        case "Piauí":
            df.loc[index, 'Região'] = "Nordeste"
        case "Maranhão":
            df.loc[index, 'Região'] = "Nordeste"
        case "Pernambuco":
            df.loc[index, 'Região'] = "Nordeste"
        case "Rio Grande do Norte":
            df.loc[index, 'Região'] = "Nordeste"
        case "Paraíba":
            df.loc[index, 'Região'] = "Nordeste"
        case "Ceará":
            df.loc[index, 'Região'] = "Nordeste"
        case "Bahia":
            df.loc[index, 'Região'] = "Nordeste"
        case "Alagoas":
            df.loc[index, 'Região'] = "Nordeste"
        case "Sergipe":
            df.loc[index, 'Região'] = "Nordeste"

        case "Mato Grosso":
            df.loc[index, 'Região'] = "Centro-Oeste"
        case "Mato Grosso do Sul":
            df.loc[index, 'Região'] = "Centro-Oeste"
        case "Goiás":
            df.loc[index, 'Região'] = "Centro-Oeste"
        case "Distrito Federal":
            df.loc[index, 'Região'] = "Centro-Oeste"

        case "São Paulo":
            df.loc[index, 'Região'] = "Sudeste"
        case "Rio de Janeiro":
            df.loc[index, 'Região'] = "Sudeste"
        case "Espírito Santo":
            df.loc[index, 'Região'] = "Sudeste"
        case "Minas Gerais":
            df.loc[index, 'Região'] = "Sudeste"

        case "Rio Grande do Sul":
            df.loc[index, 'Região'] = "Sul"
        case "Paraná":
            df.loc[index, 'Região'] = "Sul"
        case "Santa Catarina":
            df.loc[index, 'Região'] = "Sul"

        case _:
             "NaN"

df_homicidios = df[df['Tipo Crime'] == 'Homicídio doloso']

df_homicidios.to_excel('dados-tratados.xlsx')
print('Planilha crianda com sucesso.')


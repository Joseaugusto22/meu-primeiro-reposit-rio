import pandas as pd
file = "imoveis_brasil.csv"
df = pd.read_csv(file)

#exercício 01
df.head(5)
df.tail(5)

#exercício 02
df.shape

#exercício 03
df.columns

#exercício 04
df.dtypes

#exercício 05
df.describe()

#exercício 06
df.info()

#exercício 07
df.columns
df['Tipo_Imovel'].unique()

#exercício 08
df.columns
filtro = df['Valor_Imovel'] > 1000000
df.loc[filtro]

#exercício 09
coluna =['Cidade','Bairro','Valor_Imovel']
df[coluna]

#exercício 10
filtro = df["Cidade"] == "Curitiba"
df.loc[filtro]

#exercício 11
df.isnull().sum()

#exercício 12
df.sort_values("Valor_Imovel", ascending=False)

#exercício 13
df["Valor_Imovel"].mean()

#exercício 14
df["Valor_Imovel"].median()

#exercício 15
df["Valor_Imovel"].std()

#exercício 16
df.columns
df["Area_m2"].min()
df["Area_m2"].max()

#exercício 17
média = df["Valor_Imovel"].mean()
filtro = df["Valor_Imovel"] > média
df.loc[filtro]

#exercício 18
valor = df["Valor_Imovel"]
area = df["Area_m2"] 
df["valor_m2"] = valor / area

#exercício 19
dic = {"Cidade": "Teste", "Valor_Imovel" :999, "Area_m2":100}
df.loc[len(df)] = dic

#exercício 20
df.isnull().sum()

#exercício 21
filtro = df["Numero_Quartos"] !=5
df = df.loc[filtro]

#exercício 22
df.drop(columns=["ID_Imovel"])

#exercício 23
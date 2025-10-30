import streamlit as st
import pandas as pd 

st.title("meu primeiro dashboard")
st.text("Meu nome é Jose")
st.button("aperte aqui")
st.slider("Idade",0,100,25)
df = pd.read_csv("imoveis_brasil.csv")
st.dataframe(df)

import matplotlib.pyplot as plt
import pandas as pd
file="empresas_desempenho.csv"
df=pd.read_csv(file)

#gráfico de barras
df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
fig = plt.figure(figsize=(8,5))
plt.bar(df_grouped["Setor"], df_grouped["Receita"])
plt.title("Grafico de barras setor x receita")
plt.xlabel("Setor")
plt.ylabel("Receita")

st.pyplot(fig)
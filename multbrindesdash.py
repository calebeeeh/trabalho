import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as opx
from pathlib import Path
#BASE_DIR = Path(__file__).parent

# Carregar o DataFrame

st.title("Multbrindes")
st.write("Este projeto teve como objetivo organizar e digitalizar os dados de vendas da empresa MultBrindes, especializada no setor de serviços B2B e com foco em vendas para órgãos públicos. A ausência de uma sistematização eficiente dificultava a tomada de decisões estratégicas. Para solucionar esse problema, foi desenvolvido um programa de análise de dados utilizando o Pandas, associado a ferramentas como Matplotlib, Seaborn e DataFrame, aprendidas nas aulas de Programação Estruturada.")

st.write("A pesquisa adotou uma abordagem quantitativa, baseada na análise de dados fornecidos pela empresa, referentes ao período de 2019 a 2025. Após anonimização das informações, os dados foram organizados em planilhas e transformados em um dashboard interativo com gráficos de barras e de pizza, facilitando a visualização por parte da administração.")

st.write("A digitalização e análise de dados foram ferramentas fundamentais para a gestão empresarial, permitindo transformar registros brutos em insights estratégicos que orientarão decisões futuras mais assertivas.")


botaopla = st.button("planilha analisada")

arq1 = st.file_uploader("escolha um arquivo",type=["csv","xlsx","txt"])
if arq1 is not None:
    df = pd.read_excel(arq1)
    st.write("planilha carregada com sucesso!")
    multbrindes = df.copy()

multbrindes = df.copy()
if botaopla:
    botaofal = st.button("ocultar")
    st.dataframe(df)

# Seleção do tipo de gráfico
grafico_tipo = st.selectbox("Escolha o tipo de gráfico", [
    "Nenhum",
    "Barras Verticais",
    "Pizza",
    "Barras Horizontais"
])

# Gráfico de barras verticais
if grafico_tipo == "Barras Verticais":
    opcao = st.radio("Escolha o dado a visualizar:", [
        "Código Geral por Quantidade",
        "Código Geral por Lucro"
    ])

    if opcao == "Código Geral por Quantidade":
        agrupado = multbrindes.groupby("Código Geral", as_index=False)["Quantidade"].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(agrupado["Código Geral"], agrupado["Quantidade"])
        ax.set_title("Quantidade por Código Geral")
        ax.set_xlabel("Código Geral")
        ax.set_ylabel("Quantidade")
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif opcao == "Código Geral por Lucro":
        agrupado = multbrindes.groupby("Código Geral")["Lucro"].sum().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(agrupado.index, agrupado.values, color='skyblue')
        ax.set_title("Lucro por Código Geral")
        ax.set_xlabel("Código Geral")
        ax.set_ylabel("Lucro Total")
        plt.xticks(rotation=45)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

# Gráficos de pizza
elif grafico_tipo == "Pizza":
    opcao = st.radio("Escolha o dado a visualizar:", [
        "Código Geral por Lucro",
        "Código Geral por Quantidade"
    ])

    if opcao == "Código Geral por Lucro":
        agrupado = multbrindes.groupby("Código Geral")["Lucro"].sum()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(agrupado, labels=agrupado.index, autopct='%1.1f%%')
        ax.set_title("Lucro por Código Geral")
        st.pyplot(fig)

    elif opcao == "Código Geral por Quantidade":
        agrupado = multbrindes.groupby("Código Geral")["Quantidade"].sum()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(agrupado, labels=agrupado.index, autopct='%1.1f%%')
        ax.set_title("Quantidade por Código Geral")
        st.pyplot(fig)

# Gráficos de barras horizontais
elif grafico_tipo == "Barras Horizontais":
    opcao = st.radio("Escolha o dado a visualizar:", [
        "Lucro Médio por Código Geral",
        "Quantidade Média por Código Geral"
    ])

    if opcao == "Lucro Médio por Código Geral":
        agrupado = multbrindes.groupby("Código Geral")["Lucro"].mean().sort_values()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(agrupado.index, agrupado.values, color='dodgerblue')
        ax.set_title("Lucro Médio por Código Geral")
        ax.set_xlabel("Lucro Médio")
        ax.set_ylabel("Código Geral")
        st.pyplot(fig)

    elif opcao == "Quantidade Média por Código Geral":
        agrupado = multbrindes.groupby("Código Geral")["Quantidade"].mean().sort_values()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(agrupado.index, agrupado.values, color='darkorange')
        ax.set_title("Quantidade Média por Código Geral")
        ax.set_xlabel("Quantidade Média")
        ax.set_ylabel("Código Geral")
        st.pyplot(fig)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o DataFrame

st.title("Multbrindes")
st.write("A digitalização e a administração de dados no ambiente empresarial são formas estratégicas tanto para grandes quantidades de registros quanto para análises aprimoradas dos dados. No setor de serviços terceirizados, especialmente empresas voltadas para o sistema B2B ou assim como a MultBrindes que grande parte de suas vendas são voltadas para órgãos públicos, a análise estruturada de dados representa um diferencial competitivo na efetividade de processos.")

st.write("Visto que o problema central está na ausência de uma sistematização eficiente dos dados das vendas acumulados nos últimos anos, dificultando a organização e tomada de decisões estratégicas, este artigo fará o uso da ferramenta pandas, estudada nas aulas de Programação Estruturada, com intuito de aplicá-la na análise das vendas de brindes a favor de identificar oportunidades de otimização na produção e comercialização.")

st.write("O objetivo é desenvolver um programa que permita análise funcional dos dados de vendas da empresa. Ao aplicar o programa pandas e Data frame, será possível identificar quais produtos e períodos apresentam maior rentabilidade, contribuindo diretamente para o planejamento estratégico da empresa.")


botaopla = st.button("planilha analisada")

file = "C:\\Users\\calebe\\Documents\\estruturada_calebe\\multbrindes_classes.xlsx"
df = pd.read_excel(file)

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

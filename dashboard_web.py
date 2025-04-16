
import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Painel SIGED - SEMSA", layout="wide")

# Autoatualiza a cada 600 segundos (10 minutos)
st_autorefresh(interval=600000, key="refresh")

st.title("📌 Painel de Acompanhamento de Processos Prioritários - SEMSA")

df = pd.read_csv("processos_prioritarios.csv")

with st.sidebar:
    st.header("Filtros")
    unidade = st.multiselect("Unidade Responsável", options=df['unidade_responsavel'].dropna().unique())
    situacao = st.multiselect("Situação", options=df['situacao'].dropna().unique())
    if unidade:
        df = df[df['unidade_responsavel'].isin(unidade)]
    if situacao:
        df = df[df['situacao'].isin(situacao)]

st.markdown("### Lista Atualizada")
st.dataframe(df, use_container_width=True)

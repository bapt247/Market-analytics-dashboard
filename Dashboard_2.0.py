import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Config page Web
st.set_page_config(page_title = "Dashboard Multi Actifs", layout ="wide")
st.title("Dashboard d'analyse multi actifs")
st.write("Cet outil permet d'analyser le risque et la diversification des actifs")

# Extraction des données
tickers = {
    'CAC 40': '^FCHI',
    'SG' : 'GLE.PA',
    'BNP' : 'BNP.PA',
    'Or' : 'GC=F'
    }
mapping = { tickers_code : nom for nom, tickers_code in tickers.items() }
@st.cache_data
def load_data():
    df = yf.download(list(tickers.values()), period ='1y')['Close']
    df = df.rename(columns = mapping)
    df = df.dropna()
    return df
    

data = load_data()

# Calcul financier
returns =np.log(data/data.shift(1)).dropna()
vol_gliss = returns.rolling(window=30).std() *np.sqrt(252)
perf_cum = (np.exp(returns.cumsum()) - 1) * 100

# Affichage
col1, col2 = st.columns(2) # deux colonnes sur la page web
with col1:
        st.subheader("Performance cumulée (1an)")
        fig_perf =plt.figure(figsize=(10,5))
        for col in perf_cum.columns:
            plt.plot(perf_cum.index, perf_cum[col], label=col)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        st.pyplot(fig_perf)
with col2:
        st.subheader("Risque: Volatilité Glissante (30j)")
        fig_vol =plt.figure(figsize=(10,5))
        for col in vol_gliss.columns:
            plt.plot(vol_gliss.index, vol_gliss[col], label=col)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend()
        st.pyplot(fig_vol)

# Affichage Web : Matrice diversification
st.subheader("Matrice de corrélation")
matrice_corr = returns.corr()
fig_corr = plt.figure(figsize=(10,5))
sns.heatmap(matrice_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
st.pyplot(fig_corr)

import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Dashboard Ventes Livres", page_icon="📚", layout="wide")

# Chargement des données
df = pd.read_csv("best-selling-books.csv")
df = df.dropna(subset=["Genre", "FirstPublished", "Sales"])

# Sidebar - Filtres
st.sidebar.header(" Menu")

# Auteur
auteurs = st.sidebar.multiselect(
    "Choisir un ou plusieurs auteurs",
    options=df["Author"].unique(),
    default=df["Author"].unique()
)

# Langue
langues = st.sidebar.multiselect(
    "Langue originale",
    options=df["OriginalLanguage"].unique(),
    default=df["OriginalLanguage"].unique()
)

# Genre
genres = st.sidebar.multiselect(
    "Genres littéraires",
    options=df["Genre"].unique(),
    default=df["Genre"].unique()
)

# Année de publication
annee_min = int(df["FirstPublished"].min())
annee_max = int(df["FirstPublished"].max())

annees = st.sidebar.slider(
    "Plage d’années de publication",
    min_value=annee_min,
    max_value=annee_max,
    value=(1990, 2020)
)

# Application des filtres
df_filtered = df[
    (df["Author"].isin(auteurs)) &
    (df["OriginalLanguage"].isin(langues)) &
    (df["Genre"].isin(genres)) &
    (df["FirstPublished"] >= annees[0]) &
    (df["FirstPublished"] <= annees[1])
]

# === TITRE
st.title("📊 Dashboard des ventes de livres")
st.markdown("Analyse interactive basée sur les données des livres les plus vendus.")

# === KPIs dynamiques
st.subheader("📈 Indicateurs Clés de Performance (KPIs)")
col1, col2, col3, col4 = st.columns(4)

# Calculs
total_livres = len(df_filtered)
total_ventes = int(df_filtered["Sales"].sum())

livre_top = df_filtered.sort_values(by="Sales", ascending=False).iloc[0]["Book"] if total_livres > 0 else "-"
auteur_top = df_filtered["Author"].value_counts().idxmax() if total_livres > 0 else "-"

col1.metric("📚 Nombre de livres", total_livres)
col2.metric("💰 Ventes totales", f"{total_ventes:,} Exemplaires")
col3.metric("🏆 Livre le + vendu", livre_top)
col4.metric("✍️ Auteur le + prolifique", auteur_top)

st.markdown("---")

# === Graphiques interactifs
st.subheader("📊 Visualisations")

# Graphique 1 : Nombre de livres par année
fig1 = px.histogram(
    df_filtered,
    x="FirstPublished",
    nbins=20,
    title="📅 Nombre de livres publiés par année",
    labels={"FirstPublished": "Année"}
)
st.plotly_chart(fig1, use_container_width=True)

# Graphique 2 : Répartition par genre
fig2 = px.pie(
    df_filtered,
    names="Genre",
    title="📚 Répartition des livres par genre"
)
st.plotly_chart(fig2, use_container_width=True)
# === Tableau de données filtrées
st.subheader(" 📊Données filtrées")
st.dataframe(df_filtered, use_container_width=True)

# === Bouton de téléchargement
st.download_button(
    label=" Télécharger les données filtrées",
    data=df_filtered.to_csv(index=False),
    file_name="livres_filtres.csv",
    mime="text/csv"
)

st.write("Team Hatter yii")

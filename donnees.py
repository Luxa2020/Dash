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
st.subheader("Team Hatter yii Day Daww rekk")

    # Objectifs
st.subheader("🚀 Objectifs")
st.markdown("""
    - Identifier les **livres les plus performants**
    - Comprendre la **répartition par genre et par pays**
    - Suivre l’évolution du marché **dans le temps**
    - Fournir un outil interactif et facile à utiliser pour l’analyse des ventes
    """)


st.subheader("🎯 Objectif du projet")
st.write("""
    Ce projet vise à explorer et analyser les données de vente de livres à travers le monde. 
    Nous utilisons des outils de visualisation pour extraire des insights à partir de variables telles que :
    - Le titre du livre
    - L’auteur
    - L’année de publication
    - Le genre littéraire
    - Le pays d’origine
    - Le total des ventes

    Ces analyses aident à **comprendre les tendances du marché littéraire** et à **identifier les ouvrages et auteurs les plus performants**.
    """)

    # Présentation des données
st.subheader("📦 Description des données")
st.write("""
    Les données que nous utilisons contiennent les colonnes suivantes :
    - `Titre` : nom du livre
    - `Auteur` : nom de l’auteur
    - `Langue originale` : langue dans laquelle le livre a été écrit
    - `Année de publication` : année de sortie du livre
    - `Genre` : genre littéraire (roman, science-fiction, aventure, etc.)
    - `Pays d’origine` : pays de l’auteur
    - `Total des ventes` : nombre d'exemplaires vendus

    Ces données peuvent être visualisées sous forme de tableaux et de graphiques dynamiques.
    """)

    # Qu'est-ce qu'un KPI
st.subheader("📈 Que sont les KPIs ?")
st.write("""
    Les **KPI** (*Key Performance Indicators* ou **Indicateurs Clés de Performance**) sont des **mesures chiffrées** 
    qui permettent d’évaluer l’efficacité d’une activité ou d’un projet par rapport à des objectifs définis.

    Exemples de KPI dans le domaine du livre :
    - Le **livre le plus vendu**
    - Le **genre littéraire le plus populaire**
    - Le **nombre de publications par année**
    - L’**auteur le plus prolifique**

    Les KPI permettent de prendre des **décisions éclairées** grâce à une visualisation claire de la performance.
    """)

    # Importance de bien choisir les KPI
st.subheader("📌 Pourquoi bien choisir ses KPIs ?")
st.write("""
    Le choix des KPI détermine **la qualité de votre analyse**. 
    Un bon KPI doit être :
    - **Spécifique** à l’objectif
    - **Mesurable** de façon claire
    - **Pertinent** pour la décision
    - **Temporellement défini**

    Mal choisir un KPI, c’est risquer de **mal interpréter les données** et donc de prendre de mauvaises décisions.
    """)

    # Documentation du projet
st.subheader("🗂️ Documentation du projet")
st.write("""
    - 📁 Fichiers sources : `livres.csv`
    - 🧰 Bibliothèques utilisées : `Pandas`, `Plotly`, `Streamlit`
    - 📊 Visualisations : barres, histogrammes, camemberts, cartes
    - 📥 Téléchargement possible des données filtrées
    - 🗺️ Analyse géographique possible si données de pays présentes
Vous pouvez naviguer dans le menu latéral pour :
    - Explorer les KPIs
    - Filtrer les données
    - Visualiser les résultats
    - Télécharger les données
    """)

    # Objectifs
st.subheader("🚀 Objectifs")
st.markdown("""
    - Identifier les **livres les plus performants**
    - Comprendre la **répartition par genre et par pays**
    - Suivre l’évolution du marché **dans le temps**
    - Fournir un outil interactif et facile à utiliser pour l’analyse des ventes
    """)



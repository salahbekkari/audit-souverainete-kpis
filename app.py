import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Audit & KPIs Douanes & Logistique 2026",
    page_icon="🛡️",
    layout="wide"
)

# En-titre principal
st.title("🛡️ Cockpit d'Audit : Souveraineté & Performance Logistique")
st.markdown("""
**Exercice de référence : 2026** | Suivi temps réel des flux douaniers (**BADR**), portuaires (**PortNet**) et des régimes économiques (**RED**).
""")

# Sidebar pour les filtres
st.sidebar.header("🔍 Paramètres d'Analyse")
zone = st.sidebar.selectbox("Sélection Région / Terminal", ["Global (Maroc)", "Tangier Med", "Port de Casablanca", "Nador West Med"])
seuil_cible_dsm = st.sidebar.slider("Cible DUM Automatisées (%)", 50, 100, 85)

# Section Métriques Clés (KPIs)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Taux DUM Automatisées (BADR)", value="79.4%", delta="-5.6% vs Cible")
with col2:
    st.metric(label="Délai Moyen Port (Dwell Time)", value="52 h", delta="-16h (Objectif <48h)")
with col3:
    st.metric(label="Taux d'Apurement RED", value="81.2%", delta="+3.2% ce mois")
with col4:
    st.metric(label="Indice de Souveraineté Numérique", value="94.1%", delta="+1.5%")

st.markdown("---")

# Données simulées pour les graphiques
data_flux = pd.DataFrame({
    'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août'],
    'Traitement Automatisé BADR (%)': [72, 74, 76, 75, 78, 77, 80, 79.4],
    'Délai PortNet (Heures)': [68, 65, 62, 59, 57, 55, 53, 52]
})

col_gauche, col_droite = st.columns(2)

with col_gauche:
    st.subheader("📈 Évolution de l'Automatisation BADR")
    fig_badr = px.line(data_flux, x='Mois', y='Traitement Automatisé BADR (%)', markers=True, 
                       title="Progression du taux de dédouanement sans friction")
    fig_badr.add_hline(y=seuil_cible_dsm, line_dash="dash", line_color="red", annotation_text="Cible 2026")
    st.plotly_chart(fig_badr, use_container_width=True)

with col_droite:
    st.subheader("⏱️ Réduction du Dwell Time (PortNet)")
    fig_port = px.bar(data_flux, x='Mois', y='Délai PortNet (Heures)', 
                      title="Temps de séjour moyen des conteneurs (heures)")
    st.plotly_chart(fig_port, use_container_width=True)

# Tableau de synthèse des alertes réglementaires
st.subheader("🚨 Registre des Alertes et Goulots d'étranglement")
alertes_df = pd.DataFrame({
    "Indicateur / Processus": ["Passerelle Bancaire RED", "File d'attente Camions Port", "Validation Documentaire DUM", "Conformité EDI PortNet"],
    "Statut": ["Attention", "Critique", "Conforme", "Optimal"],
    "Délai de Résolution Estimé": ["48 heures", "Immédiat", "N/A", "N/A"],
    "Impact Risque": ["Moyen", "Élevé", "Faible", "Faible"]
})
st.table(alertes_df)

# Pied de page
st.markdown("---")
st.markdown("*Plateforme d'audit et de pilotage opérationnel — Conçue pour l'optimisation des flux douaniers et portuaires.*")

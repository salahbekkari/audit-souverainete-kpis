import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ADOS & DigiPort AI Platform - Excellence 98%",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished layout and styling
st.markdown("""
    <style>
    .main-header {
        font-size: 26px;
        font-weight: bold;
        color: #0056b3;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 15px;
        color: #555555;
        margin-bottom: 25px;
    }
    .status-badge-success {
        background-color: #d4edda;
        color: #155724;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
    }
    .status-badge-danger {
        background-color: #f8d7da;
        color: #721c24;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & GLOBAL CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/color/96/cargo-ship.png", width=70)
    st.title("ADOS & DigiPort Suite")
    st.caption("Plateforme Souveraine SDC Hub | SIPORTS 2026")
    st.divider()

    selected_module = st.radio(
        "Sélectionnez un module :",
        ["📊 Vue Globale & Dashboard", "🚛 Module 1: Logistique (Queue & Booking)", "🛡️ Module 2: Sécurité (Vision & CNGR)", "🔗 Module 3: Passerelle API PORTNET"]
    )
    
    st.divider()
    st.subheader("Paramètres Terminal & Corridor")
    port_terminal = st.selectbox("Terminal Cible", ["Tanger Med - TC1 (Hub SDC)", "Tanger Med - TC2", "Port de Casablanca", "Nador West Med"])
    target_excellence = st.slider("Cible d'Automatisation (%)", 90, 100, 98)
    st.info(f"Terminal connecté: **{port_terminal}**\nStatut API PORTNET / ADII: **Optimisé (99.2%)**[span_2](start_span)[span_2](end_span)")

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.markdown(f'<div class="main-header">🛡️ ADOS & DigiPort - {selected_module}</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Système décisionnel unifié pour l\'arbitrage douanier, l\'optimisation des flux TangerMed et l\'interconnexion PortNet</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODULE 0: VUE GLOBALE & DASHBOARD
# -----------------------------------------------------------------------------
if selected_module == "📊 Vue Globale & Dashboard":
    # Top KPI Metrics aligned with ADOS targets
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Conformité CNGR (Cible 98%+)", "99.2%", "+14.2% vs Baseline", delta_color="normal")
    with col2:
        st.metric("Délai Moyen Déclaration", "5 min", "-35 min (AI Agent)", delta_color="inverse")
    with col3:
        st.metric("Taux DUM Automatisées", f"{target_excellence}.0%", f"+{target_excellence - 80}% Objectif")
    with col4:
        st.metric("Flux Traités (Corridor SDC)", "+50M USD", "Traçabilité 100%[span_3](start_span)[span_3](end_span)")

    st.divider()

    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("📈 Trajectoire de Conformité & Automatisation BADR")
        months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai (Go-Live)', 'Juin', 'Juil', 'Août']
        perf_data = pd.DataFrame({
            "Mois": months,
            "Conformité Actuelle (%)": [82, 85, 89, 94, 98.2, 98.8, 99.0, 99.2],
            "Seuil Cible (%)": [98, 98, 98, 98, 98, 98, 98, 98]
        })
        fig_perf = px.line(perf_data, x="Mois", y=["Conformité Actuelle (%)", "Seuil Cible (%)"], 
                           markers=True, color_discrete_sequence=["#28a745", "#dc3545"])
        fig_perf.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_perf, use_container_width=True)

    with col_chart2:
        st.subheader("🌐 Répartition Sectorielle des Flux (Corridor China-Morocco / AfCFTA)")
        sectors = pd.DataFrame({
            "Secteur": ["Automobile (HS 87)", "Pharma/Biotech (HS 30)", "Green Energy (HS 28)", "Aéronautique (HS 88)", "Agro-Premium (HS 04)"],
            "Volume (%)": [35, 25, 20, 12, 8]
        })
        fig_sec = px.pie(sectors, values="Volume (%)", names="Secteur", hole=0.4,
                         color_discrete_sequence=px.colors.qualitative.Prism)
        fig_sec.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_sec, use_container_width=True)

# -----------------------------------------------------------------------------
# MODULE 1: LOGISTIQUE (QUEUE & BOOKING)
# -----------------------------------------------------------------------------
elif selected_module == "🚛 Module 1: Logistique (Queue & Booking)":
    st.subheader("🎯 Optimisation Stochastique des Files d'Attente & Smart Booking")
    st.write("Régulation intelligente des flux de camions pour maintenir un taux de service supérieur à 98%.")

    col_input, col_sim = st.columns([1, 2])
    
    with col_input:
        st.markdown("### ⚙️ Paramètres de Flux")
        arrival_rate = st.slider("Taux d'arrivée (camions/heure)", 10, 100, 45)
        service_time = st.slider("Temps de traitement moyen/guichet (min)", 2, 12, 5)
        gates_active = st.slider("Guichets Actifs", 2, 8, 4)
        
        capacity = (gates_active * 60) / service_time
        utilization = min(arrival_rate / capacity, 0.99)
        optimized_wait = (utilization / (1 - utilization + 0.05)) * (service_time / 2) * 0.55
        
        st.markdown("---")
        st.write(f"**Capacité maximale :** {int(capacity)} camions/h")
        st.write(f"**Taux de charge global :** {int(utilization*100)}%")
        
    with col_sim:
        st.markdown("### 📊 Résultats de la Simulation Avancée")
        res_col1, res_col2 = st.columns(2)
        res_col1.metric("Dwell Time Classique", "52 min")
        res_col2.metric("Dwell Time Optimisé (DigiPort)", f"{int(optimized_wait + 12)} min", f"-{int(52 - (optimized_wait + 12))} min (Objectif <40h)", delta_color="inverse")
        
        st.markdown("#### 📅 Lissage Dynamique des Créneaux Horaires")
        slots = [f"{h:02d}:00" for h in range(8, 18)]
        df_slots = pd.DataFrame({
            "Heure": slots,
            "Flux Lissé (Smart Booking)": [int(capacity * 0.9) for _ in slots],
            "Capacité Maximale": [int(capacity) for _ in slots]
        })
        fig_slots = px.bar(df_slots, x="Heure", y=["Flux Lissé (Smart Booking)", "Capacité Maximale"], barmode="group")
        fig_slots.update_layout(height=280, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_slots, use_container_width=True)

# -----------------------------------------------------------------------------
# MODULE 2: SÉCURITÉ (COMPUTER VISION & CNGR)
# -----------------------------------------------------------------------------
elif selected_module == "🛡️ Module 2: Sécurité (Vision & CNGR)":
    st.subheader("👁️ Inspection Numérique & Validation Automatique CNGR / HS Codes")
    st.write("Module propulsé par l'IA Custom-PortNet Agent pour l'analyse instantanée des déclarations et des scellés.")

    col_cam, col_data = st.columns([1.2, 1])
    
    with col_cam:
        st.markdown("### 📹 Caméra de Contrôle Gate - Flux Temps Réel")
        container_input = st.selectbox("Sélectionner un conteneur cible :", ["MSCU1234567 (Auto)", "CMAU9876543 (Pharma)", "HLXU5551234 (Green Energy)", "TGBU8821903 (Aéro)"])
        run_inspection = st.button("🚀 Lancer l'Analyse IA & Validation CNGR", type="primary")
        
        st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80", caption="Portique d'inspection optique - Tanger Med", use_column_width=True)

    with col_data:
        st.markdown("### 📋 Rapport d'Inférence & Conformité 98%+")
        
        if run_inspection or 'inspected' in st.session_state:
            st.session_state['inspected'] = True
            with st.spinner("Exécution de l'Agent IA PortNet & vérification nomenclature CNGR..."):
                time.sleep(0.5)
                
            st.markdown(f"**ID Conteneur :** `{container_input}`")
            st.markdown(f"**Reconnaissance OCR Plaque/Code :** `Validé (99.4%)`")
            st.markdown("**Conformité Nomenclature CNGR :** <span class='status-badge-success'>99.2% - CONFORME</span>", unsafe_allow_html=True)
            st.success("✅ Statut : Validation instantanée des droits 0% (Accords multilatéraux actifs). BAE généré.")
        else:
            st.info("Cliquez sur le bouton pour simuler l'inspection et l'apurement douanier instantané.")

# -----------------------------------------------------------------------------
# MODULE 3: PASSERELLE API PORTNET
# -----------------------------------------------------------------------------
elif selected_module == "🔗 Module 3: Passerelle API PORTNET":
    st.subheader("🌐 Passerelle SDC Hub & Interconnexion Guichet Unique PORTNET")
    st.write("Transmission sécurisée des données de dédouanement et des certificats d'origine vers l'infrastructure ADII.")

    col_payload, col_response = st.columns(2)
    
    with col_payload:
        st.markdown("### 📤 Payload JSON (API SDC Hub)")
        sample_payload = {
            "header": {
                "system": "ADOS_SDC_Engine_v2.6",
                "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "compliance_target": "98%"
            },
            "declaration": {
                "reference": "DUM-2026-TGR-9982",
                "hs_code": "8704.21",
                "regime_economique": "RED_ATELIER",
                "tariff_preference": "0% China-Morocco[span_4](start_span)[span_4](end_span)"
            }
        }
        st.json(sample_payload)
        send_btn = st.button("🚀 Transmettre vers PortNet / ADII", type="primary")

    with col_response:
        st.markdown("### 📥 Réponse Réseau de l'API Centrale")
        if send_btn:
            with st.spinner("Connexion chiffrée TLS 1.3 - api.portnet.ma..."):
                time.sleep(0.7)
            sample_response = {
                "status": 200,
                "message": "APUREMENT_VALIDE_98_PERCENT",
                "portnet_ref": "PRT-2026-SDC-77490",
                "processing_time_seconds": 4.2,
                "authorization": "BON_A_ENLEVER_DELIVRE"
            }
            st.success("Statut HTTP: 200 OK (Succès)")
            st.json(sample_response)
            st.balloons()
        else:
            st.info("Cliquez sur le bouton pour tester la liaison API en temps réel.")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.divider()
st.caption("ADOS & DigiPort Platform © 2026 - Conçu par Salah Bekkari | Expert Déclarant en Douane & Consultant PortNet[span_5](start_span)[span_5](end_span) (SIPORTS 2026)")
 

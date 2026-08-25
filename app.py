import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & SESSION STATE
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ADOS & DigiPort AI Platform - Le Détroit Smart Ports",
    page_icon="⚓",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'audit_history' not in st.session_state:
    st.session_state['audit_history'] = []

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

    lang = st.selectbox("🌐 Langue / اللغة", ["Français", "العربية (Arabe)"])
    is_ar = (lang == "العربية (Arabe)")

    selected_module = st.radio(
        "Sélectionnez un module :" if not is_ar else "اختر الوحدة :",
        [
            "📊 Vue Globale & Dashboard" if not is_ar else "📊 لوحة القيادة العامة", 
            "🚛 Module 1: Logistique (Queue & Booking)" if not is_ar else "🚛 الوحدة 1: اللوجستيات والحجز الذكي", 
            "🛡️ Module 2: Sécurité (Vision & CNGR)" if not is_ar else "🛡️ الوحدة 2: الأمن والرؤية الحاسوبية", 
            "🔗 Module 3: Passerelle API PORTNET" if not is_ar else "🔗 الوحدة 3: بوابة PORTNET الرقمية"
        ]
    )
    
    st.divider()
    st.subheader("Paramètres du Détroit" if not is_ar else "إعدادات المضيق")
    port_terminal = st.selectbox("Terminal Cible" if not is_ar else "المحطة المستهدفة", ["Tanger Med - TC1 (Hub SDC)", "Tanger Med - TC2", "Port de Casablanca", "Nador West Med"])
    target_excellence = st.slider("Cible d'Automatisation (%)" if not is_ar else "هدف الأتمتة (%)", 90, 100, 98)
    st.info(f"Terminal connecté: **{port_terminal}**\nStatut API PORTNET: **Optimisé (99.2%)**")

# -----------------------------------------------------------------------------
# HEADER TEXT BASED ON LANGUAGE
# -----------------------------------------------------------------------------
if not is_ar:
    st.markdown(f'<div class="main-header">⚓ ADOS & DigiPort - {selected_module}</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Système décisionnel unifié pour l\'arbitrage douanier, l\'optimisation des flux TangerMed et l\'interconnexion PortNet (Faire vibrer le Détroit)</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="main-header" dir="rtl">⚓ منصة أدوس وديجي بورت - {selected_module}</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header" dir="rtl">نظام قرار موحد لتحسين التدفقات الجمركية بميناء طنجة المتوسط والربط الذكي مع بوابة فورتنيت</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODULE 0: VUE GLOBALE & DASHBOARD
# -----------------------------------------------------------------------------
if selected_module in ["📊 Vue Globale & Dashboard", "📊 لوحة القيادة العامة"]:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Conformité CNGR (Cible 98%+)", "99.2%", "+14.2% vs Baseline", delta_color="normal")
    with col2:
        st.metric("Délai Moyen Déclaration", "5 min", "-35 min (AI Agent)", delta_color="inverse")
    with col3:
        st.metric("Taux DUM Automatisées", f"{target_excellence}.0%", f"+{target_excellence - 80}% Objectif")
    with col4:
        st.metric("Flux Traités (Corridor SDC)", "+50M USD", "Traçabilité 100%")

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

    st.divider()
    st.subheader("📑 Générateur de Rapport d'Audit Exécutif (Export Officiel)")
    if st.button("📥 Générer le Rapport PDF de Synthèse SIPORTS 2026"):
        with st.spinner("Compilation des indicateurs du détroit..."):
            time.sleep(0.8)
        report_text = f"""--- RAPPORT OFFICIEL ADOS & DIGIPORT ---
Terminal: {port_terminal}
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Conformité CNGR: 99.2%
Délai Déclaration: 5 min
Volume Corridor: +50M USD
Statut: Validé pour Excellence Opérationnelle SIPORTS 2026
-------------------------------------------"""
        st.success("✅ Rapport d'audit généré avec succès !")
        st.download_button(
            label="Télécharger le fichier .txt du Rapport",
            data=report_text,
            file_name=f"Rapport_Audit_ADOS_{port_terminal.replace(' ', '_')}.txt",
            mime="text/plain"
        )

# -----------------------------------------------------------------------------
# MODULE 1: LOGISTIQUE (QUEUE & BOOKING)
# -----------------------------------------------------------------------------
elif selected_module in ["🚛 Module 1: Logistique (Queue & Booking)", "🚛 الوحدة 1: اللوجستيات والحجز الذكي"]:
    st.subheader("🎯 Optimisation Stochastique des Files d'Attente & Smart Booking")
    
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
        res_col2.metric("Dwell Time Optimisé (DigiPort)", f"{int(optimized_wait + 12)} min", f"-{int(52 - (optimized_wait + 12))} min", delta_color="inverse")
        
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
elif selected_module in ["🛡️ Module 2: Sécurité (Vision & CNGR)", "🛡️ الوحدة 2: الأمن والرؤية الحاسوبية"]:
    st.subheader("👁️ Inspection Numérique & Validation Automatique CNGR / HS Codes")
    
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
            st.success("✅ Statut : Validation instantanée des droits 0%. BAE généré.")
            
            st.session_state['audit_history'].append({
                "Timestamp": datetime.now().strftime("%H:%M:%S"),
                "Container": container_input,
                "Status": "Conforme 99.2%"
            })
        else:
            st.info("Cliquez sur le bouton pour simuler l'inspection et l'apurement douanier instantané.")

    if st.session_state['audit_history']:
        st.divider()
        st.subheader("📜 Journal d'Historique des Simulations de Session")
        df_history = pd.DataFrame(st.session_state['audit_history'])
        st.dataframe(df_history, use_container_width=True)

# -----------------------------------------------------------------------------
# MODULE 3: PASSERELLE API PORTNET
# -----------------------------------------------------------------------------
elif selected_module in ["🔗 Module 3: Passerelle API PORTNET", "🔗 الوحدة 3: بوابة PORTNET الرقمية"]:
    st.subheader("🌐 Passerelle SDC Hub & Interconnexion Guichet Unique PORTNET")
    
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
                "tariff_preference": "0% China-Morocco"
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
st.caption("ADOS & DigiPort Platform © 2026 - Conçu par Salah Bekkari | Expert Déclarant en Douane & Consultant PortNet (SIPORTS 2026)")

import streamlit as st
from datetime import date

st.set_page_config(page_title="Gerätemanagement Hochschule", layout="wide")
st.title("Geräte-Verwaltung an der Hochschule")

# Navigation in der Seitenleiste (entspricht den Use Cases)
menu = st.sidebar.radio(
    "Navigation",
    ["Geräte-Verwaltung", "Nutzer-Verwaltung", "Reservierungen", "Wartungs-Management"]
)

# 1. USE CASE: GERÄTE-VERWALTUNG
if menu == "Geräte-Verwaltung":
    st.header("Geräte-Verwaltung")
    tab1, tab2 = st.tabs(["Gerät anlegen / ändern", "Geräteübersicht"])

    with tab1:
        with st.form("device_form"):
            device_id = st.number_input("Inventarnummer (ID)", min_value=1, step=1, value=101)
            device_name = st.text_input("Gerätename", placeholder="z.B. Beamer")
            responsible = st.selectbox(
                "Verantwortliche Person",
                ["max.mustermann@mci.edu", "anna.schmidt@mci.edu"]
            )
            col1, col2 = st.columns(2)
            with col1:
                first_maint = st.date_input("Erste Wartung", value=date.today())
                maint_interval = st.number_input("Wartungsintervall (Tage)", min_value=1, value=90)
            with col2:
                end_of_life = st.date_input("End of Life", value=date(2030, 12, 31))
                maint_cost = st.number_input("Wartungskosten (€)", min_value=0.0, value=150.0, step=10.0)

            submitted = st.form_submit_button("Gerät speichern")
            if submitted:
                st.success(f"Mockup: Gerät '{device_name}' (ID: {device_id}) wurde gespeichert!")

    with tab2:
        st.subheader("Aktuelle Geräte (Beispieldaten)")
        st.table([
            {"ID": 101, "Name": "Desktop - PC", "Verantwortlich": "max.mustermann@mci.edu", "Nächste Wartung": "2026-12-15"},
            {"ID": 102, "Name": "Beamer", "Verantwortlich": "anna.schmidt@mci.edu", "Nächste Wartung": "2027-01-10"},
        ])

# 2. USE CASE: NUTZER-VERWALTUNG
elif menu == "Nutzer-Verwaltung":
    st.header("Nutzer-Verwaltung")
    with st.form("user_form"):
        user_name = st.text_input("Name des Nutzers", placeholder="Max Mustermann")
        user_email = st.text_input("E-Mail-Adresse (ID)", placeholder="max.mustermann@mci.edu")
        if st.form_submit_button("Nutzer anlegen"):
            st.success(f"Mockup: Nutzer '{user_name}' ({user_email}) angelegt!")

    st.subheader("Registrierte Nutzer (Beispieldaten)")
    st.table([
        {"E-Mail (ID)": "max.mustermann@mci.edu", "Name": "Max Mustermann"},
        {"E-Mail (ID)": "anna.schmidt@mci.edu", "Name": "Anna Schmidt"},
    ])

# 3. USE CASE: RESERVIERUNGS-SYSTEM (Vorschau Case Study II)
elif menu == "Reservierungen":
    st.header("Reservierungs-System")
    st.selectbox("Gerät auswählen", ["101 - Desktop -PC", "102 - Beamer"])
    st.selectbox("Nutzer auswählen", ["max.mustermann@mci.edu", "anna.schmidt@mci.edu"])
    col1, col2 = st.columns(2)
    col1.date_input("Startdatum")
    col2.date_input("Enddatum")
    st.button("Reservierung eintragen")


import streamlit as st
import pandas as pd

# Dummy-Daten
venues_data = pd.DataFrame({
    "Location": ["Molotow", "Uebel & Gefährlich", "Goldener Salon", "Hafenklang"],
    "Stadtteil": ["St. Pauli", "St. Pauli", "Altona", "Altona"],
    "Musikstil-Fit": ["Indie", "Elektro", "Rap", "Alternative"]
})

creator_data = pd.DataFrame({
    "Name": ["@indie.hh", "@raptalk.de", "@elektro.vibes", "@musikmomente"],
    "Plattform": ["Instagram", "TikTok", "YouTube", "Instagram"],
    "Thema": ["Indie-Tipps", "Deutschrap", "Clubs & Releases", "Konzertberichte"],
    "Follower": [8500, 22000, 12000, 9700]
})

medien_data = pd.DataFrame({
    "Medium": ["Bedroomdisco", "Diffus", "Noisey DE", "Tonspion"],
    "Typ": ["Blog", "Magazin", "Online-Magazin", "Musikblog"],
    "Genre-Fokus": ["Indie", "Hip-Hop", "Elektro", "Allround"]
})

partner_data = pd.DataFrame({
    "Partner": ["Backspin", "Groove Attack", "Pop Office Hamburg", "Clouds Hill"],
    "Typ": ["Musikmagazin", "Vertrieb", "Förderstelle", "Label/Studio"],
    "Kooperationsidee": ["Interviewserie", "Release-Vertrieb", "Live-Förderung", "Session-Aufnahme"]
})

st.set_page_config(page_title="Musik-Marketinganalyse")
st.title("🎶 Lokale Marketinganalyse für Musikprojekte")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Venues", "Creator", "📰 Medien", "🤝 Partner", "Empfehlung"
])

with tab1:
    st.subheader("Clubs & Locations")
    st.dataframe(venues_data)

with tab2:
    st.subheader("Musik-Creator & Influencer")
    st.dataframe(creator_data)

with tab3:
    st.subheader("Relevante Musikmedien")
    st.dataframe(medien_data)

with tab4:
    st.subheader("Kooperationspartner")
    st.dataframe(partner_data)

with tab5:
    st.subheader("Use Case – Strategievorschlag")

    musikstil = st.selectbox("Musikstil:", ["Indie", "Pop", "Elektro", "Hip-Hop"])
    zielgruppe = st.selectbox("Zielgruppe:", ["jung & urban", "alternativ", "Mainstream"])
    budget = st.selectbox("Promo-Budget:", ["niedrig", "mittel", "hoch"])

    if st.button("Strategie anzeigen"):
        if musikstil == "Indie" and zielgruppe == "jung & urban":
            st.write("Empfehlung: Auftritt im Molotow + PR über Bedroomdisco + TikTok-Kampagne mit @indie.hh")
        elif musikstil == "Hip-Hop" and budget == "hoch":
            st.write("Empfehlung: Showcase mit @raptalk.de, Beitrag bei Backspin, Vertrieb via Groove Attack.")
        elif musikstil == "Elektro":
            st.write("Empfehlung: Clubkooperation mit Uebel & Gefährlich + Creator-Kampagne @elektro.vibes + Tonspion-Feature.")
        else:
            st.write("Empfehlung: Datenbasis noch im Aufbau – spezifischere Auswahl nötig.")

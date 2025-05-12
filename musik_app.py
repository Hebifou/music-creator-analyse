import streamlit as st
import pandas as pd

# Dummy-Daten
venues_data = pd.DataFrame({
    "Location": ["Molotow", "Uebel & Gefährlich", "Goldener Salon", "Hafenklang"],
    "Stadtteil": ["St. Pauli", "St. Pauli", "Altona", "Altona"],
    "Musikstil-Fit": ["Indie", "Elektro", "Hip-Hop", "Indie"]
})

creator_data = pd.DataFrame({
    "Name": ["@indie.hh", "@raptalk.de", "@elektro.vibes", "@musikmomente"],
    "Plattform": ["Instagram", "TikTok", "YouTube", "Instagram"],
    "Thema": ["Indie-Tipps", "Deutschrap", "Clubs & Releases", "Konzertberichte"],
    "Musikstil": ["Indie", "Hip-Hop", "Elektro", "Indie"],
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
    "Musikstil": ["Hip-Hop", "Elektro", "Indie", "Indie"],
    "Kooperationsidee": ["Interviewserie", "Release-Vertrieb", "Live-Förderung", "Session-Aufnahme"]
})

# Auswahl-Tab
st.set_page_config(page_title="Musik-Marketinganalyse")
st.title("🎶 Marketing-Analyse für Musikprojekte")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Auswahl", "Venues", "Creator", "Medien", "Empfehlung"
])

with tab1:
    st.subheader("Dein Release-Profil")
    musikstil = st.selectbox("Musikstil", ["Indie", "Pop", "Hip-Hop", "Elektro"])
    zielgruppe = st.selectbox("Zielgruppe", ["jung & urban", "alternativ", "Mainstream"])
    budget = st.selectbox("Budget", ["niedrig", "mittel", "hoch"])
    st.success("Auswahl gespeichert – wechsle die Tabs für passende Empfehlungen")

with tab2:
    st.subheader("Clubs & Venues – passend zu deinem Musikstil")
    st.dataframe(venues_data[venues_data["Musikstil-Fit"] == musikstil])

with tab3:
    st.subheader("Creator-Vorschläge")
    st.dataframe(creator_data[creator_data["Musikstil"] == musikstil])

with tab4:
    st.subheader("Musikmedien & Blogs")
    st.dataframe(medien_data[(medien_data["Genre-Fokus"] == musikstil) | (medien_data["Genre-Fokus"] == "Allround")])

with tab5:
    st.subheader("Empfohlene Gesamtstrategie")

    if musikstil == "Indie" and zielgruppe == "jung & urban":
        st.markdown("""
        - **Venue:** Molotow  
        - **Creator:** @indie.hh  
        - **Medium:** Bedroomdisco  
        - **Partner:** Pop Office Hamburg  
        - **Strategie:** Showcase + TikTok + Blogartikel + Förderung
        """)
    elif musikstil == "Elektro":
        st.markdown("""
        - **Venue:** Uebel & Gefährlich  
        - **Creator:** @elektro.vibes  
        - **Medium:** Tonspion  
        - **Partner:** Groove Attack  
        - **Strategie:** Club-Feature + Creator-Reel + Vertriebsdeal
        """)
    else:
        st.info("Für diese Kombination werden gerade Empfehlungen ergänzt.")

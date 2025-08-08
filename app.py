#!/usr/bin/env python3

# app.py
import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("sanjay_sabha_playlist_data.xlsx")

df = load_data()

st.title("🎵 Welcome to Sanjay Sabha Search")

st.markdown("🔍 **Enter song name, raga, or composer to search:**")

query = st.text_input("Search ▶️").strip().lower()

if query:
    results = df[df.apply(lambda row: query in str(row).lower(), axis=1)]

    st.markdown(f"✅ **Found {len(results)} match(es):**\n")

    for _, row in results.iterrows():
        st.markdown(f"""
        ---
        🎶 **{row['Title']}**
        🎼 *Raga:* {row.get('Raga', 'N/A')}
        🧑‍🎤 *Composer:* {row.get('Composer', 'N/A')}
        📺 *Season {row.get('Season', 'N/A')} Episode {row.get('Episode', 'N/A')}* @ {row.get('Timestamp', 'N/A')}
        🔗 [Watch on YouTube]({row.get('YouTube URL', '#')})
        """)
else:
    st.info("Type something to search (e.g., **sahana**, **dikshitar**, **RTP**).")

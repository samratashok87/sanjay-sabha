#!/usr/bin/env python3

# app.py
import streamlit as st
import pandas as pd

def time_to_seconds(timestamp):
    parts = timestamp.split(':')
    parts = list(map(int, parts))
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h = 0
        m, s = parts
    else:
        h = 0
        m = 0
        s = parts[0]
    return h*3600 + m*60 + s

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
        start_seconds = time_to_seconds(row['Timestamp'])
        video_url_with_time = f"{row['YouTube URL']}&t={start_seconds}s"
        st.markdown(f"""
        ---
        🎶 **{row['Title']}**
        🎼 *Raga:* {row.get('Raga', 'N/A')}
        🧑‍🎤 *Composer:* {row.get('Composer', 'N/A')}
        📺 *Season {row.get('Season', 'N/A')} Episode {row.get('Episode', 'N/A')}* @ {row.get('Timestamp', 'N/A')}
        🔗 [Watch on YouTube]({video_url_with_time})
        """)
else:
    st.info("Type something to search (e.g., **sahana**, **dikshitar**, **RTP**).")

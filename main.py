# main.py
"""
Ce fichier est le point d'entrée principal de l'application Streamlit.
Il initialise l'interface utilisateur et gère le flux global de l'application.
Il interagit principalement avec ui.py pour l'affichage et youtube_transcript.py pour la logique métier.
"""

import streamlit as st
from ui import create_ui
from youtube_transcript import extract_transcript
from config import load_config

def main():
    # Chargement de la configuration
    config = load_config()
    
    # Création de l'interface utilisateur
    url = create_ui()
    
    # Si une URL est fournie, on extrait le transcript
    if url:
        try:
            transcript = extract_transcript(url)
            st.success("Transcript extrait avec succès!")
            st.text_area("Transcript:", value=transcript, height=300)
        except Exception as e:
            st.error(f"Erreur lors de l'extraction du transcript: {str(e)}")

if __name__ == "__main__":
    main()
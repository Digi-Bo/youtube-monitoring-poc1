# ui.py
"""
Ce fichier contient les composants de l'interface utilisateur Streamlit.
Il définit les fonctions pour créer et afficher les éléments de l'interface.
Il interagit principalement avec main.py pour fournir l'interface utilisateur.
"""

import streamlit as st

def create_ui():
    """
    Crée l'interface utilisateur principale de l'application.
    
    :return: L'URL de la vidéo YouTube entrée par l'utilisateur
    """
    st.title("Extracteur de Transcripts YouTube")
    
    # Champ de saisie pour l'URL de la vidéo
    url = st.text_input("Entrez l'URL de la vidéo YouTube:")
    
    # Bouton pour déclencher l'extraction
    if st.button("Extraire le transcript"):
        if url:
            return url
        else:
            st.warning("Veuillez entrer une URL valide.")
    
    return None

# Ajoutez ici d'autres fonctions pour créer des éléments d'interface utilisateur si nécessaire
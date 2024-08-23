# config.py
"""
Ce fichier gère la configuration de l'application.
Il charge les variables d'environnement et définit les constantes globales.
Il interagit avec le fichier .env pour récupérer les informations sensibles.
"""

import os
from dotenv import load_dotenv

def load_config():
    """
    Charge la configuration de l'application.
    
    :return: Un dictionnaire contenant la configuration
    """
    # Chargement des variables d'environnement depuis le fichier .env
    load_dotenv()
    
    # Création d'un dictionnaire de configuration
    config = {
        "API_KEY": os.getenv("YOUTUBE_API_KEY"),
        # Ajoutez ici d'autres variables de configuration si nécessaire
    }
    
    return config
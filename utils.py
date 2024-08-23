# utils.py
"""
Ce fichier contient des fonctions utilitaires génériques.
Ces fonctions peuvent être utilisées dans différentes parties de l'application.
Il fournit des outils pour le formatage, la validation, et d'autres tâches communes.
"""

import re

def extract_video_id(url):
    """
    Extrait l'ID de la vidéo à partir d'une URL YouTube.
    
    :param url: L'URL de la vidéo YouTube
    :return: L'ID de la vidéo
    """
    # Utilisation d'une expression régulière pour extraire l'ID de la vidéo
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("ID de vidéo non trouvé dans l'URL fournie")

# Ajoutez ici d'autres fonctions utilitaires si nécessaire
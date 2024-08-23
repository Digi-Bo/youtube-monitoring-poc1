# youtube_transcript.py
"""
Ce fichier gère toutes les opérations liées à l'extraction des transcripts YouTube.
Il contient la logique pour extraire l'ID de la vidéo et récupérer le transcript.
Il utilise l'API YouTube Transcript et interagit avec utils.py pour certaines fonctions utilitaires.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from utils import extract_video_id

def extract_transcript(url):
    """
    Extrait le transcript d'une vidéo YouTube à partir de son URL.
    
    :param url: L'URL de la vidéo YouTube
    :return: Le transcript sous forme de texte
    """
    try:
        # Extraction de l'ID de la vidéo à partir de l'URL
        video_id = extract_video_id(url)
        
        # Récupération du transcript via l'API YouTube Transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Conversion du transcript en texte continu
        transcript_text = " ".join([entry['text'] for entry in transcript])
        
        return transcript_text
    except Exception as e:
        # En cas d'erreur, on la propage pour qu'elle soit gérée dans main.py
        raise Exception(f"Erreur lors de l'extraction du transcript: {str(e)}")
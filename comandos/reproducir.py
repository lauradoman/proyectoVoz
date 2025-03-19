from utils.hablar import hablar
import webbrowser
import time
from googleapiclient.discovery import build
from utils.estado import set_escuchar  # Para controlar el estado de escucha

# Tu clave de API de YouTube Data API
API_KEY = 'AIzaSyAxTLN4MqKy7l4o174RApwlxETOXgoixHY'

# Inicializa el cliente de la API de YouTube
youtube = build('youtube', 'v3', developerKey=API_KEY)

def abrir_video_youtube(consulta):
    """Realiza una búsqueda en YouTube con la consulta dada y reproduce el primer resultado."""
    consulta = consulta.replace("reproduce", "").strip()  # Eliminar la palabra "buscar"
    
    set_escuchar(False)  # Desactivar la escucha mientras se procesa la búsqueda
    hablar(f"buscando {consulta} en YouTube...")

    # Realiza la búsqueda en YouTube usando la API
    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=consulta
    )
    
    response = request.execute()

    if 'items' in response and len(response['items']) > 0:
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        # Abrir el primer resultado de la búsqueda en YouTube
        webbrowser.open(video_url)
        hablar(f"Reproduciendo el primer video")
    else:
        hablar(f"No se encontraron resultados para {consulta}")
    
    hablar(f"¿Necesitas algo más?")
    
    # Esperar un tiempo para permitir que el asistente se recupere
    time.sleep(2)  # O puedes reemplazar esto con un ciclo que verifique la disponibilidad de escucha.
    
    set_escuchar(True)  # Reactivar la escucha después de que haya terminado

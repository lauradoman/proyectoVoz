from utils.hablar import hablar
import webbrowser
import time
from utils.estado import set_escuchar  # Para controlar el estado de escucha

def buscar(consulta):
    """Realiza una búsqueda en Google con la consulta dada."""
    consulta = consulta.replace("buscar", "").strip() 
    set_escuchar(False)
    hablar(f"Buscando {consulta} en Google...")

    # Desactivar la escucha mientras se realiza la búsqueda
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)
    
    hablar(f"¿Necesitas algo más?")
    
    # Esperar un tiempo para permitir que el asistente se recupere
    time.sleep(2)  # O puedes reemplazar esto con un ciclo que verifique la disponibilidad de escucha.
    
    # Reactivar la escucha después de que haya terminado
    set_escuchar(True)

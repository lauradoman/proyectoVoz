# utils/hablar.py
from gtts import gTTS
import os
import pygame
from utils.estado import set_escuchar  # Para manejar el estado de escucha

# Inicializamos pygame para la reproducción de audio
pygame.init()

def hablar(texto):
    """Convierte texto a voz y lo reproduce usando gTTS."""
    try:
        # Antes de hablar, desactivar la escucha para evitar conflictos
        set_escuchar(False)

        # Convertir el texto a voz con gTTS
        tts = gTTS(text=texto, lang='es')
        
        # Guardar el archivo de audio temporalmente
        audio_file = 'audio_respuesta.mp3'
        tts.save(audio_file)
        
        # Reproducir el archivo de audio
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        # Esperar a que termine de reproducir
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Eliminar el archivo de audio temporal después de reproducirlo
        os.remove(audio_file)

        # Una vez que haya terminado de hablar, activar la escucha nuevamente
        set_escuchar(True)

    except gTTS.lang.tts.gTTSError as e:
        print(f"Error de gTTS: {e}")
    except pygame.error as e:
        print(f"Error en pygame: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
        set_escuchar(True)  # Asegurarse de restaurar la escucha si ocurre un error

# utils/escuchar.py
import speech_recognition as sr
from utils.hablar import hablar
from utils.estado import get_escuchar  # Para obtener el estado de escuchando
from utils.estado import set_escuchar
import time

def reconocer_voz(ejecutar_comando):
    """Función que escucha comandos de voz y los ejecuta."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            # Solo escucha si el estado está habilitado
            if not get_escuchar():
                continue  # Si no está escuchando, no procesa nada

            try:
                print("Escuchando...")
                audio = recognizer.listen(source, timeout=10)
                comando = recognizer.recognize_google(audio, language="es-ES").lower()
                print(f"Comando recibido: {comando}")

                ejecutar_comando(comando)

            except sr.UnknownValueError:
                hablar("No entendí, puedes repetirlo?")
                time.sleep(2)
                set_escuchar(True)
            except sr.RequestError:
                hablar("Hubo un error con el reconocimiento de voz.")
                time.sleep(2)
                set_escuchar(True)
            except Exception as e:
                hablar(f"Ocurrió un error: {str(e)}")
                time.sleep(2)
                set_escuchar(True)



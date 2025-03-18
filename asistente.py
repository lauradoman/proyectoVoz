
import pyttsx3
import speech_recognition as sr
import webbrowser
from comandos.ejecutar_comando import ejecutar_comando  # Importamos desde comandos
import time  # Para poder usar time.sleep

# Función para configurar el motor de voz
def configurar_voz():
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)  # Velocidad del habla

    voices = engine.getProperty('voices')
    for voice in voices:
        if "spanish" in voice.name.lower():  # Buscar una voz en español
            engine.setProperty("voice", voice.id)
            return engine  # Devuelve el motor configurado con la voz en español

    return engine  # Si no encuentra voz en español, devuelve el motor con la voz por defecto


# Función para que el asistente hable
def hablar(engine, mensaje):
    print(f"Asistente: {mensaje}")
    engine.say(mensaje)
    engine.runAndWait()


# Función para reconocer comandos de voz
def reconocer_voz(engine):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:  # Bucle infinito para seguir escuchando
            hablar(engine, "Te escucho...")
            recognizer.adjust_for_ambient_noise(source)

            try:
                # Establecer un tiempo de espera máximo de 15 segundos
                audio = recognizer.listen(source, timeout=10)  # Espera un máximo de 15 segundos
                comando = recognizer.recognize_google(audio, language="es-ES").lower()
                print(f"Comando: {comando}")
                ejecutar_comando(engine, comando)  # Ejecutamos el comando recibido

            except sr.UnknownValueError:
                hablar(engine, "No entendí, ¿puedes repetirlo?")

            except sr.RequestError:
                hablar(engine, "Hubo un error con el reconocimiento de voz.")

            except Exception as e:
                hablar(engine, f"Ocurrió un error: {str(e)}")

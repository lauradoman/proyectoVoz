
import pyttsx3

# Inicializar el motor de pyttsx3
engine = pyttsx3.init()

# Obtener la lista de voces disponibles
voices = engine.getProperty("voices")

# Buscar y configurar la voz en español
voice_found = False
for voice in voices:
    if "spanish" in voice.name.lower():  # Buscar una voz en español
        engine.setProperty("voice", voice.id)
        voice_found = True
        break

if not voice_found:
    print("No se encontró una voz en español. Usando la predeterminada.")
else:
    print("Voz en español configurada correctamente.")

# Establecer la velocidad
engine.setProperty("rate", 150)

# Probar con un mensaje
engine.say("Hola, este es un mensaje en español.")
engine.runAndWait()

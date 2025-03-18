
from asistente import configurar_voz, hablar, reconocer_voz

# Función para activar el asistente al ejecutar el archivo
def activar_asistente():
    engine = configurar_voz()  # Configura el motor de voz
    
    # Verificamos si el motor se ha configurado correctamente
    if engine is None:  
        print("Error: No se pudo configurar el motor de voz.")
        return
    
    hablar(engine, "Asistente activado. ¿En qué puedo ayudarte?")
    reconocer_voz(engine)

# Ejecutar el asistente
if __name__ == "__main__":
    activar_asistente()  # Llamamos a la función para activar el asistente

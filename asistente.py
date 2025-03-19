from utils.escuchar import reconocer_voz
from comandos.ejecutar_comando import ejecutar_comando

def activar_asistente():
    """Función que inicia el asistente."""
    reconocer_voz(ejecutar_comando)

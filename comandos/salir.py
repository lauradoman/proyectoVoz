from utils.estado import set_escuchar
import sys
from utils.hablar import hablar

def salir_comando():
    """Desactiva la escucha y cierra el asistente."""
    print("Desactivando escucha.")
    set_escuchar(False)
    hablar("adios,buen dia")
    sys.exit()# Desactiva la escucha

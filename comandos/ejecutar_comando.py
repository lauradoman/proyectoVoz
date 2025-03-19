from comandos.buscar import buscar  # Si tienes un comando de búsqueda
from comandos.salir import salir_comando  # Si tienes un comando de salir
from utils.estado import set_escuchar 

def ejecutar_comando(comando):
    """Procesa el comando y ejecuta la acción correspondiente."""
    
    comando = comando.lower()  # Convertir a minúsculas para evitar problemas de mayúsculas
    
    if "buscar" in comando:
        # Si el comando incluye la palabra "buscar", ejecuta la búsqueda
        buscar(comando)
    
    elif "salir" in comando:
        # Si el comando incluye la palabra "salir", ejecuta la acción para salir
        salir_comando()
    
    elif "no gracias" in comando:
        # Si el comando incluye la palabra "salir", ejecuta la acción para salir
        salir_comando()
    else:
        # Si no se reconoce el comando, notifica al usuario
        print(f"Comando no reconocido: {comando}")


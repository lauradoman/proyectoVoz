from comandos.buscar import buscar  # Si tienes un comando de búsqueda
from comandos.salir import salir_comando  # Si tienes un comando de salir
from utils.estado import set_escuchar
import inspect

def ejecutar_comando(comando):
    """Procesa el comando y ejecuta la acción correspondiente."""
    
    comando = comando.lower()  # Convertir a minúsculas para evitar problemas de mayúsculas

    # Diccionario de comandos con funciones que requieren o no argumentos
    comandos = {
        "buscar": buscar_comando,  # Función que recibe argumento
        "salir": salir_comando,    # Función que no recibe argumento
        "no gracias": salir_comando,  # Función que no recibe argumento
    }

    # Recorre el diccionario para encontrar el comando y ejecutarlo
    for clave, funcion in comandos.items():
        if clave in comando:
            # Verificar si la función requiere un argumento
            if len(inspect.signature(funcion).parameters) > 0:
                funcion(comando)  # Si requiere argumento, pasa el comando
            else:
                funcion()  # Si no requiere argumento, ejecuta la función sin parámetros
            break
    else:
        # Si no se reconoce el comando, notifica al usuario
        print(f"Comando no reconocido: {comando}")


def buscar_comando(comando):
    """Función que maneja el comando de búsqueda."""
    # Llama a la función de búsqueda (pasando el comando)
    buscar(comando)

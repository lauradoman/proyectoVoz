
from comandos.buscar import buscar
from comandos.salir import salir

def ejecutar_comando(engine, comando):
    if "buscar" in comando:
        consulta = comando.replace("buscar", "").strip()
        buscar(consulta, engine)
    elif "salir" in comando:
        salir(engine)
    else:
        engine.say("No tengo ese comando programado.")
        engine.runAndWait()

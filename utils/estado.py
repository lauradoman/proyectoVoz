# utils/estado.py

# Variable global que indica si el asistente está escuchando
escuchando = True

def set_escuchar(estado: bool):
    global escuchando
    escuchando = estado

def get_escuchar():
    return escuchando

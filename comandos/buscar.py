
import webbrowser

def buscar(consulta, engine):
    url = f"https://www.google.com/search?q={consulta.replace(' ', '+')}"
    engine.say(f"Buscando {consulta} en Google")
    engine.runAndWait()
    webbrowser.open(url)

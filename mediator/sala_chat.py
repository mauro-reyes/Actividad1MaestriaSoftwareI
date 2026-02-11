class SalaChat:
    def __init__(self):
        self.historial = []

    def enviar_mensaje(self, mensaje, remitente):
        registro = f"[{remitente}]: {mensaje}"
        self.historial.append(registro)

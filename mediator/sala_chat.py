# el patron mediator centraliza la comunicación entre usuarios
# evita dependencias directas entre colegas
class SalaChat:
    def __init__(self):
        self.historial = []
        self.usuarios = {}

    def registrar_usuario(self, usuario):
        if usuario.nombre not in self.usuarios:
            self.usuarios[usuario.nombre] = usuario

    def enviar_mensaje(self, mensaje, remitente):
        registro = f"[{remitente}]: {mensaje}"
        self.historial.append(registro)
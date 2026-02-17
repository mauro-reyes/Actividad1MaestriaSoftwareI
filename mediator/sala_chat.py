# el patron mediator centraliza la comunicación entre usuarios
# evita dependencias directas entre colegas
class SalaChat:
    def __init__(self):
        self._historial = []
        self._usuarios = {}

    @property
    def usuarios(self):
        return self._usuarios
    
    @usuarios.setter
    def usuarios(self, value):
        self._usuarios = value

    @property
    def historial(self):
        return self._historial

    def registrar_usuario(self, usuario):
        if usuario.nombre not in self._usuarios:
            self._usuarios[usuario.nombre] = usuario

    def enviar_mensaje(self, mensaje, remitente):
        registro = f"[{remitente}]: {mensaje}"
        self._historial.append(registro)
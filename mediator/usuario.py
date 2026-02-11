class Usuario:
    def __init__(self, nombre, mediador):
        self.nombre = nombre
        self.mediador = mediador

    def enviar(self, mensaje):
        self.mediador.enviar_mensaje(mensaje, self.nombre)

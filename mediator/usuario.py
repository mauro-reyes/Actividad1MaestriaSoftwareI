#clase usuario que delega la comunicación al mediador
#No mantiene referencais a otros usuarios.
class Usuario:
    def __init__(self, nombre, mediador):
        self.nombre = nombre
        self.mediador = mediador
        self.mediador.registrar_usuario(self)

    def enviar(self, mensaje):
        self.mediador.enviar_mensaje(mensaje, self.nombre)

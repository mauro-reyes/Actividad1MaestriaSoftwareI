#clase usuario que delega la comunicación al mediador
#No mantiene referencais a otros usuarios.
class Usuario:
    def __init__(self, nombre, mediador):
        self._nombre = nombre
        self._mediador = mediador
        self._mediador.registrar_usuario(self)

    @property
    def nombre(self):
        return self._nombre

    def enviar(self, mensaje):
        self._mediador.enviar_mensaje(mensaje, self.nombre)

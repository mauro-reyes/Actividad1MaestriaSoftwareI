#Abstracción del patron bridge manteniendo una referencia a la implementación
from abc import ABC, abstractmethod
from bridge.plataforma import Plataforma

class Notificacion(ABC):

    def __init__(self, plataforma: Plataforma):
        self._plataforma = plataforma

    @abstractmethod
    def emitir(self, mensaje: str) -> str:
        pass

class AlertaCritica(Notificacion):
    def emitir(self, mensaje: str) -> str:
        return f"{self._plataforma.enviar(mensaje)}"

class MensajeInformativo(Notificacion):
    def emitir(self, mensaje: str) -> str:
        return f"{self._plataforma.enviar(mensaje)}"
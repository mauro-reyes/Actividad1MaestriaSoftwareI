#implementación del patron bridge. Se define la interfaz com[un para todas las plataformas.
from abc import ABC, abstractmethod

class Plataforma(ABC):

    @abstractmethod
    def enviar(self, contenido: str) -> str:
        pass

class Web(Plataforma):
    def enviar(self, contenido: str) -> str:
        return f"[Web] Renderizando en DOM: {contenido}"

class Movil(Plataforma):
    def enviar(self, contenido: str) -> str:
        return f"[Móvil] Notificación Push enviada: {contenido}"
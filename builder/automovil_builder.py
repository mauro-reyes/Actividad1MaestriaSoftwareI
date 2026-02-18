#Define la interfaz para la construcción paso a paso del objeto Automovil.
#permite separar el proceso de construcción de su representación final.
from abc import ABC, abstractmethod
from builder.automovil import Automovil

class AutomovilBuilder(ABC):

    @abstractmethod
    def set_motor(self, motor): pass

    @abstractmethod
    def set_color(self, color): pass

    @abstractmethod
    def set_llantas(self, llantas): pass

    @abstractmethod
    def set_gps(self, gps): pass

    @abstractmethod
    def set_techo(self, techo): pass

    @abstractmethod
    def build(self): pass


class AutomovilBuilderConcreto(AutomovilBuilder):

    def __init__(self):
        self._motor = "Estándar"
        self._color = "Blanco"
        self._llantas = "R15"
        self._gps = False
        self._techo = False

    def set_motor(self, motor):
        self._motor = motor
        return self

    def set_color(self, color):
        self._color = color
        return self

    def set_llantas(self, llantas):
        self._llantas = llantas
        return self

    def set_gps(self, gps):
        self._gps = gps
        return self

    def set_techo(self, techo):
        self._techo = techo
        return self

    def build(self):
        return Automovil(
            self._motor,
            self._color,
            self._llantas,
            self._gps,
            self._techo
        )

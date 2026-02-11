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
        self.motor = "Estándar"
        self.color = "Blanco"
        self.llantas = "R15"
        self.gps = False
        self.techo = False

    def set_motor(self, motor):
        self.motor = motor
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_llantas(self, llantas):
        self.llantas = llantas
        return self

    def set_gps(self, gps):
        self.gps = gps
        return self

    def set_techo(self, techo):
        self.techo = techo
        return self

    def build(self):
        return Automovil(
            self.motor,
            self.color,
            self.llantas,
            self.gps,
            self.techo
        )

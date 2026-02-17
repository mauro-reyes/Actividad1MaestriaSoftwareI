#Producto complejo que contiene multiples configuraciones de forma opcional
#se construye a través del patrón builder para evitar constructores teslescópicos.
class Automovil:
    def __init__(self, motor, color, llantas, gps, techo):
        self._motor = motor
        self._color = color
        self._llantas = llantas
        self._gps = gps
        self._techo = techo

    @property
    def motor(self):
        return self._motor

    @property
    def color(self):
        return self._color

    @property
    def llantas(self):
        return self._llantas

    @property
    def gps(self):
        return self._gps

    @property
    def techo(self):
        return self._techo

#Producto complejo que contiene multiples configuraciones de forma opcional
#se construye a través del patrón builder para evitar constructores teslescópicos.
class Automovil:
    def __init__(self, motor, color, llantas, gps, techo):
        self.motor = motor
        self.color = color
        self.llantas = llantas
        self.gps = gps
        self.techo = techo


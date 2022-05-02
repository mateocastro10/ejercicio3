class Registro:
    __humedad = 0
    __temp = 0.0
    __presion = 0
    def __init__(self, h, t, p):
        self.__humedad = h
        self.__temp = t
        self.__presion = p
    def dpresion(self):
        return int(self.__presion)
    def dhumedad(self):
        return int(self.__humedad)
    def dtemp(self):
        return float(self.__temp)

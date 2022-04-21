class ViajeroFrecuente
    def __init__(self, nv, d, n, a , ma):
        self.__num_viajero = nv
        self.__dni = d
        self.__nombre = n
        self.__apellido = a
        self.__millas_acum = ma
    def cantidadTotalMillas(self):
        return self.__millas_acum
    def acumularmillas(self, xc):
        self.__millas_acum += xc
        return self.__millas_acum
    def canjear(self, mac):
        if self.__millas_acum >= mac
            return self.__millas_acum
        else print("ERROR")


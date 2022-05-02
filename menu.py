from ManejadorRegistro import Lista
class claseMenu:
    __op=0
    def __init__(self):
        self.__op=None
    def opcion(self,op,mr):
        if op==1:
            self.opcion1(mr)
        elif op==2:
            self.opcion2(mr)
        elif op==3:
            self.opcion3(mr)
        elif op == 4:
            self.salir()

    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, mr):
        mr.muestra()


    def opcion2(self, mr):
        mr.promedio()

    def opcion3(self, mr):
        dia= int(input('Ingrese dia a consultar'))
        mr.listadovariables(dia)

from claseRegistro import Registro
import csv

class Lista:
    def __init__(self):
        self.__listaRegistro = [[Registro for i in range(30)] for j in range(24)]

    def __str__(self):
        s = ''
        for Registro in self.__listaRegistro:
            s += str(Registro) + '\n'
        return s

    def agregarReg(self, unReg, x, y):
        if type(unReg==Registro)and type(x==int)and type(y==int):
            self.__listaRegistro[y][x] = unReg
        else:
            print('PARAMETRO INCORRECTO')

    def testReg(self):
        archivo = open('datos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            d = int(fila[0])
            ho = int(fila[1])
            t = float(fila[2])
            h = int(fila[3])
            p = int(fila[4])
            unReg = Registro(h, t, p)
            self.agregarReg(unReg, d-1, ho-1)
        archivo.close()

    def muestra(self):
        menorp = 9999
        diamenorp = 0
        horamenorp = 0
        mayorp = 0
        diamayorp = 0
        horamayorp = 0
        menorh = 9999
        diamenorh = 0
        horamenorh = 0
        mayorh = 0
        diamayorh = 0
        horamayorh = 0
        menort = 9999
        diamenort = 0
        horamenort = 0
        mayort = 0
        diamayort = 0
        horamayort = 0
        for i in range(24):
            for j in range(30):
                x = self.__listaRegistro[i][j].dpresion()
                if x < menorp:
                    menorp = x
                    diamenorp = i
                    horamenorp = j
                elif x > mayorp:
                    mayorp = x
                    diamayorp = i
                    horamayorp = j
                y = self.__listaRegistro[i][j].dhumedad()
                if y < menorh:
                    menorh = y
                    diamenorh = i
                    horamenorh = j
                elif y > mayorh:
                    mayorh = y
                    diamayorh = i
                    horamayorh = j
                z = self.__listaRegistro[i][j].dtemp()
                if z < menort:
                    menort = z
                    diamenort = i
                    horamenort = j
                if z > mayort:
                    mayort = z
                    diamayort = i
                    horamayort = j

        print('EL DIA {} A LAS {}HS SE REGISTRO LA MENOR PRESION, LA CUAL FUE DE: {}'.format(diamenorp+1, horamenorp+1, menorp))
        print('EL DIA {} A LAS {}HS SE REGISTRO LA MAYOR PRESION, LA CUAL FUE DE: {}'.format(diamayorp+1, horamayorp+1, mayorp))
        print('EL DIA {} A LAS {}HS SE REGISTRO LA MENOR HUMEDAD, LA CUAL FUE DE: {}'.format(diamenorh+1, horamenorh+1, menorh))
        print('EL DIA {} A LAS {}HS SE REGISTRO LA MAYOR HUMEDAD, LA CUAL FUE DE: {}'.format(diamayorh+1, horamayorh+1, mayorh))
        print('EL DIA {} A LAS {}HS SE REGISTRO LA MENOR TEMPERATURA, LA CUAL FUE DE: {}'.format(diamenort+1, horamenort+1, menort))
        print('EL DIA {} A LAS {}HS SE REGISTRO LA MAYOR TEMPERATURA, LA CUAL FUE DE: {}'.format(diamayort+1, horamayort+1, mayort))

    def promedio(self):
        for i in range(24):
            prom=0
            for j in range(30):
                z = self.__listaRegistro[i][j].dtemp()
                prom+=z
            print('HORA {}: {}'.format(i+1, prom/30))

    def listadovariables(self, dia):
        print('HORA TEMPERATURA HUMEDAD PRESION')
        for i in range(24):
            print('{}      {}       {}      {}'.format(i+1, self.__listaRegistro[i][dia-1].dtemp(), self.__listaRegistro[i][dia-1].dhumedad(), self.__listaRegistro[i][dia-1].dpresion()))

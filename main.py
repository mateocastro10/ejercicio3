from ManejadorRegistro import Lista
from menu import claseMenu
if __name__ == '__main__':
    mr = Lista()
    mr.testReg()
    xmenu = claseMenu()
    b = False
    while not b:
        print('-------MENU DE OPCIONES-------')
        print(
            'opcion 1: Mostrar para cada variable el día y hora de menor y mayor valor \nopcion 2: Indicar la temperatura promedio mensual por cada hora.\nopcion 3: listar los valores de las tres variables para cada hora del día dado.\n opcion 4:salir')
        op = int(input('seleccione opcion'))
        if op == 0 or op>4:
            print('OPCION INCORRECTA')
        else:
            b = True
            xmenu.opcion(op, mr)



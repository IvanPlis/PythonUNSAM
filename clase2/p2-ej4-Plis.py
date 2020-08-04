"""
Ejercicio 4. Tablas de multiplicar. Escriba un programa que imprima de forma elegante las tablas de
multiplicar del 0 al 9 (sug: imprimir ’\t’ como separador). Si puede, evite usar la multiplicaci´on, use solo
sumas.
"""


def printTablas():
    acum = 0
    for i in range(1, 10):
        for j in range(10):
            acum = acum + i
            print(acum, "-")
        acum = 0
        print('\t')


printTablas()

"""
Ejercicio 2. Dominó: Escribir una función que indique si dos fichas de dominó son compatibles o no,
para el caso en que ... (Nota: utilizar la función split() para las cadenas.)
a) Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
b) Las fichas son recibidas en una cadena, por ejemplo: '3-4 2-5'.
"""

def fichas_compatibles(ficha1, ficha2):

    izq=0
    der=1

    if (ficha1[izq]==ficha2[der] or ficha1[der]==ficha2[izq]
            or ficha1[izq]==ficha2[izq] or ficha1[der]==ficha2[der]):
        print("jugada permitida")
    else:
        print("jugada invalida")

ficha1 = ('3', '4')
ficha2 = ('4', '5')
ficha3 = ('3', '6')
ficha4 = ('2', '6')

fichas_compatibles(ficha1, ficha2)
fichas_compatibles(ficha1, ficha3)
fichas_compatibles(ficha2, ficha3)
fichas_compatibles(ficha3, ficha4)

"""
a) Suponga que vamos a armar parejas para viajar en un automovil, de manera que la primer persona
listada maneja y la segunda es copiloto. Genere la lista de todas las parejas ordenadas que se puede
formar entre estas cuatro personas (aca s ́ı imorta el orden).

b)Genere todas las palabras de 2 letras (con o sin sentido, con o sin letras repetidas) que usen solo las
letras ’ABCDE’.

c) Genere todas las palabras de 5 letras (con o sin sentido, sin letras repetidas) que usen solo las letras
’ABCDE’
"""

import itertools


def ejercicioA(personas):
    combOrdenadas = list(itertools.permutations(personas, 2))
    for persona in combOrdenadas:
        print("Piloto: %s | Copiloto: %s" % (persona[0], persona[1]))
    print("\t")


def ejercicioB(letras):
    letrasCombinadas = list(itertools.combinations_with_replacement(letras, 5))
    for letra in letrasCombinadas:
        print("%s%s%s%s%s" % (letra[0], letra[1], letra[2], letra[3], letra[4]))


def ejercicioC(letras):
    letrasCombinadas = list(itertools.permutations(letras, 5))
    for letra in letrasCombinadas:
        print("%s%s%s%s%s" % (letra[0], letra[1], letra[2], letra[3], letra[4]))


personas = ['Andrada', 'Alonso', 'Pol', 'Campuzano']
ejercicioA(personas)
letras = ['A', 'B', 'C', 'D', 'E']
ejercicioB(letras)
ejercicioC(letras)

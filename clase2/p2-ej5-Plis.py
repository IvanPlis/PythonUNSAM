"""
Ejercicio 5. Men´u a la carta. El men´u de un restaurante se compone de una entrada, un plato principal
y un postre. Las entradas son cinco para elegir (digamos ensalada, camarones, guacamole, lengua o
humus). An´alogamente, hay cinco platos principales y cinco postres (arme sus listas segun gustos persona-
les). Usando simplemente ciclos (y no la librer´ıa itertools)
Imprima todas las combinaciones posibles de menues que se pueden armar.
Modiﬁque el programa (sin alterar las listas) para que imprima ´unicamente las combinaciones que
una persona vegetariana comer´ıa.
Si alguien come todos los d´ıas en ese restaurante y no quiere comer el mismo plato dos veces en
una semana: imprima cinco men´ues de forma que esta persona pruebe todas las entradas, platos
principales y postres a lo largo de una semana. (sugerencia: usar pop()).
"""


def printCombinaciones(entrada, principal, postre):
    i = 0
    j = 0
    k = 0
    for servirEnt in entrada:
        for servirPri in principal:
            for servirPostre in postre:
                k = k + 1
                print("Combinacion ", i + j + k, ": ", servirEnt, "-", servirPri, "-", servirPostre)


def menuVegetariano(entrada, principal, postre):
    entradaV = []
    principalV = []
    postreV = []
    i = 0
    for servirEnt in entrada:
        if servirEnt != 'camarones' and servirEnt != 'lengua':
            i = i + 1
            entradaV.append(servirEnt)
    for servirPri in principal:
        if servirPri != 'bondiola' and servirPri != 'riniones' and servirPri != 'milanesa':
            principalV.append(servirPri)
    for servirPostre in postre:
        if servirPostre != 'flan' and servirPostre != 'helado':
            postreV.append(servirPostre)

    printCombinaciones(entradaV, principalV, postreV)


def noRepetirMenu(entrada, principial, postre):
    i = 0
    for servirEnt in entrada:
        for servirPri in principal:
            for servirPostre in postre:
                print("Combinacion ", i, ": ", servirEnt, "-", servirPri, "-", servirPostre)
                i = i + 1
                postre.remove(servirPostre)
                break
            principal.remove(servirPri)
            break
        entrada.remove(servirEnt)
        continue


entrada = ['ensalada', 'camarones', 'guacamole', 'lengua', 'humus']
principal = ['bondiola', 'riniones', 'tofu', 'milanesa', 'espinaca']
postre = ['flan', 'manzana', 'banana', 'helado', 'caramelos']

printCombinaciones(entrada, principal, postre)
print('\t')
menuVegetariano(entrada, principal, postre)
print('\t')
noRepetirMenu(entrada, principal, postre)

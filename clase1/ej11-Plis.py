# Ejercicio 11. Determine los errores de los siguientes codigos y corrijalos. ¿Que tipo de errores tiene cada uno?#

"""
---codigo 1---
Error en tiempo de ejecucion: Retornaba False si la primera letra no era vocal.
Modificado para que retorne false al final si no encotntro ninguna vocal.
"""


def tiene_a(palabra):
    n = len(palabra)
    i = 0
    while i < n:
        if palabra[i] == 'a':
            return True
        # else:
        # return False#
        i += 1
    return False


str1 = "hola"
print("codigo 1:", tiene_a(str1))

"""
---codigo 2----
Error en tiempo de compilacion: 
Faltaban los ':' para definir la funcion y en los if y while
En el if se esta asignando un char en vez de comprobar igualdad. Agregado el '=='
"""


# def tiene_n(palabra)
def tiene_a2(palabra):
    n = len(palabra)
    i = 0
    # while i<n
    while i < n:
        # if palabra[i]='a'
        if palabra[i] == 'a':
            return True
        i += 1
    return False


str2 = "jefe"
print("codigo 2:", tiene_a2(str2))

""""
---codigo 3---
Error en tiempo de compilacion: '1984' esta definido como un integer, lo que genera una incositencia en los tipos 
de datos
"""


def tiene_uno(palabra):
    n = len(palabra)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if palabra[i] == '1':
            tiene = True
        i += 1
    return tiene


# tiene_uno(1984)#
print("codigo 3:", tiene_uno('UNSAM 2020')
      , tiene_uno('La novela 1984 de George Orwell')
      , tiene_uno('1984'))

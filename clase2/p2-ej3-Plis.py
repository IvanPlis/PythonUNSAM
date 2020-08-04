"""
Ejercicio 3. Buscar un string dentro de otro. Escriba un programa que, dados dos strings devuelva
(si existe) la posici ́on del primero dentro del segundo.
Por ejemplo: si s1 = "Paseo el perro por la vereda" y s2 = "perro", el resultado ser ́a 9.
"""


def getPosString(longS, shortS):
    contAux = 0
    pos = -1
    yaEsta = False

    for i in range(len(longS)):

        if longS[i] == shortS[contAux] and contAux <= len(shortS):
            contAux = contAux + 1

            if contAux == len(shortS):
                break

            if (yaEsta == False):
                yaEsta = True
                pos = i

        else:
            yaEsta = False
            contAux = 0
            pos = -1

    return pos


str1 = input("Ingrese cadena: ")
str2 = input("Ingrese subcadena: ")
print("El string esta contenido en la posicion i =", getPosString(str1, str2))

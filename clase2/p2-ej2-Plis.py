"""
Dada una frase S y usando for e if (pero no m ́etodos propios de str que resuelvan el
problema de una), escriba un programa que#
1-Convierta a may ́uscula la primera letra de cada palabra de la frase.1
2-Elimine espacios de la frase.
3-Elimine espacios, convirtiendo la letra siguiente a may ́uscula.
4-Y por  ́ultimo un programa que invierta el proceso: tome la frase pegoteada recien generada y regenere
la frase original con espacios y sin may ́usculas.#
"""

def toMayus(S):
    newS = ""
    space = True

    for letra in S:
        if space == True:
            newS = newS + chr(ord(letra) - 32)
            space = False
        elif letra == ' ':
            space = True
            newS = newS + letra
        else:
            newS = newS + letra

    return newS


def deleteSpace(S):
    newS = ""
    for letra in S:
        if letra != ' ':
            newS = newS + letra
    return newS


def toMayusNoSpace(S):
    sMayus = toMayus(S)
    newS = deleteSpace(sMayus)
    return newS


def getOriginal(S, S3):
    oldS = ""

    for i, letra in enumerate(S3):
        if letra == chr(ord(S[i]) + 32):
            oldS = oldS + chr(ord(S[i-aux]) + 32)
        elif S[i] == ' ':
            oldS = oldS + ' ' + letra
            aux=aux+1
        else:
            oldS = oldS + letra

    return oldS


S = input("Ingrese frase (toda en minusculas): ")
S1 = toMayus(S)
S2 = deleteSpace(S)
S3 = toMayusNoSpace(S)
S4 = getOriginal(S, S3)
print(S1)
print(S2)
print(S3)
print(S4)
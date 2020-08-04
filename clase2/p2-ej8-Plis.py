"""
Ejercicio 8. Rehaga el ejercicio de la gu ́ıa anterior que toma una cadena de caracteres y cambia todas
las vocales por - usando como  ́unico ciclo el comando for c in palabra:
"""

def cambiarVocales(str):
    nuevoStr=""
    reemplazo='-'
    for c in str:
        if c == 'a' or c== 'e' or c == 'i' or c== 'o' or c == 'u':
            nuevoStr=nuevoStr+reemplazo
        else:
            nuevoStr=nuevoStr+c
    return nuevoStr


str="hola master que haces"
print(str)
str=cambiarVocales(str)
print(str)
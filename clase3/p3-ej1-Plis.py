"""
Ejercicio 1. Escribir una función que reciba una tupla de elementos e indique si se encuentran
ordenados de menor a mayor o no. p.ej ('algo','nada','poco') ó (1,45,3.45,-1) Nota:
el orden de las cadenas (strings) es lexicográfico
"""


def is_tupla_sorted(tupla):
    for i in range(len(tupla) - 1):
        if tupla[i] >= tupla[i + 1]:
            print("La tupla no esta ordenada")
            return False
    print("La tupla esta ordenada")
    return True


tupla = ('algo', 'poco', 'nada')
tupla2 = ('boca', '1', 'river')
tupla3 = ('1', 'boca', 'river')

print(is_tupla_sorted(tupla))
print(is_tupla_sorted(tupla2))
print(is_tupla_sorted(tupla3))

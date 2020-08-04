"""
Ejercicio 11. Escriba una funcion tal que, dado un vector y un
elemento determine si el elemento est ́a en el vector o no, y si est ́a que devuelva su posicíon.
Ejercicio 12. Idem pero con busqueda binaria
"""


def busqueda_secuencial(vector, elemento):
    """busca elemento recorriendo una a una las pocisiones del vector"""
    cont = 0

    for i in range(len(vector)):
        cont = i
        if vector[i] == elemento:
            print("Numero de pasos busqueda secuencial:", cont)
            return i

    print("Numero de pasos busqueda secuencial:", cont)
    return -1


def busqueda_binaria(vector, elemento):
    """Implementa el algoritmo de busqueda binario para encontrar un elemento en un vector"""

    vector = bubble_sort(vector)    #Ordeno el vector
    first = 0
    last = len(vector) - 1
    i = 0

    while first < last:
        i += 1
        medio = (first + last) // 2     #Redondeo la mitad por truncamiento

        if vector[medio] == elemento:
            print("Numero de pasos busqueda binaria:", i)
            return medio
        elif vector[medio] < elemento:
            first = medio + 1   #Al trabajar con cantidades discretas la proxima
                                #considero el elemento de al lado para ahorrar pasos
        else:
            last = medio - 1

    print("Numero de pasos busqueda binaria:", i)
    return -1


def bubble_sort(vector):
    """Implementa el algoritmo de ordenamiento burbuja"""
    n = len(vector)
    aux = 0

    for i in range(n):
        for j in range(0, n - 1):
            if vector[j] > vector[i]:
                aux = vector[i]     #guardo uno de los elementos a swappear
                vector[i] = vector[j]
                vector[j] = aux

    return vector


vector = [5, 6, 7, 22, 1, 9, 45, 4]

print(vector)
print(bubble_sort(vector))
print("Elemento encontrado en la posicion:", busqueda_secuencial(vector, 9))
print("Elemento encontrado en la posicion:", busqueda_secuencial(vector, 8))
print("Elemento encontrado en la posicion:", busqueda_binaria(vector, 9))
print("Elemento encontrado en la posicion:", busqueda_binaria(vector, 8))

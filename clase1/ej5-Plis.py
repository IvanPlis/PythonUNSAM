# Ejercicio 5. Defina una funcion que tome dos cadenas de caracteres como parametro y devuelva la de mayor longitud.#

def masLarga(str1, str2):
    if len(str1) > len(str2):
        res = str1
    elif len(str1) < len(str2):
        res = str2
    else:
        res = "ninguna"
    return res


str1 = input("Ingrese cadena 1: ")
str2 = input("Ingrese cadena 2: ")

res = masLarga(str1, str2)
print(res)

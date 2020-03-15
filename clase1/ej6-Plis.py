# Defina una funcion que recibe una cadena de caracteres y devuelve la cantidad de letras que contiene#

def cant_e(str1):
    i = 0
    count = 0
    while i < len(str1):
        if str1[i] == 'e':
            count = count + 1
        i = i + 1
    return count


str1 = input("Ingrese cadena: ")
cant_e = cant_e(str1)
print("Hay", cant_e, "letras e en la cadena ingresada")

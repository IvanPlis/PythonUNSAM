# Ejercicio 7. Defina una funcion que tome una cadena de caracteres y cambie todas las vocales por - #

def replaceVowels(str1):
    i = 0
    count = 0
    str2 = str1.lower()  # Convierto a minuscalas para optimizar nro de comprobaciones
    str1 = list(str1)   # Transformo a lista para poder reemplazar vocales
    while i < len(str2):
        if str2[i] == 'a' or str2[i] == 'e' or str2[i] == 'i' or str2[i] == 'o' or str2[i] == 'u':
            str1[i]= '-'    #Reemplazo en la cadena original para no alterar consonantes mayusculas
        i = i + 1
    str1= "".join(str1) #Reconvierto lista a string
    return str1


str1 = input("Ingrese cadena: ")
str1 = replaceVowels(str1)

print(str1)

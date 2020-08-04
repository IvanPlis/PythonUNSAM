#Ejercicio 1. Escriba un programa que enumere los elementos de la lista [Pyhton, C++, C, Pascal].#

list=["Python", "C++", "C", "Pascal"]
for enum, letra in enumerate (list):
    print(enum, letra)
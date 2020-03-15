#Ejercicio 4. Escriba un script que pregunte el radio r de una esfera y calcule su volumen, 43πr3. Ejecute
# el script desde la linea de comandos para responder ¿cual es el volumen de una esfera de radio 6?#

import math

def getVolEsfera (radio):
    volEsfera = (4 / 3) * math.pi * radio ** 3
    return volEsfera

radio=int(input("Ingrese radio: "))
volEsfera=getVolEsfera(radio)
print("El volumen de la esfera es", volEsfera)

volEsfera=getVolEsfera(6)
print("El volumen de la esfera de radio 6 es", volEsfera)
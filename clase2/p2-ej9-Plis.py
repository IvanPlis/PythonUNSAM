x = 25
epsilon = 0.01
paso = epsilon**2
sol = 0.0
totPasos = 0

while abs(sol**2 -x) >= epsilon and sol<x: #Salgo cuando hallo la solucion con poco error o cuando me paso
    sol += paso
    totPasos+= 1
    if abs(sol**2 -x) < epsilon: #si encontre la solucion
        print("La raiz de %f es %f"%(x,sol))
        print("La solucion fue encontrada en %d pasos"%totPasos)
    else:
        print("Luego de %d pasos no encontre la solucion"%totPasos)
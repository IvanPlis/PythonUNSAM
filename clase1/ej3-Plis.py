#Ejercicio 3. Si corre una carrera de 6 millas en 42 minutos 42 segundos, ¿cual fue tu velocidad promedio en km/h?#

distMillas=6
tiempoMin=42
tiempoSeg=42

segTot=tiempoSeg+(tiempoMin*60)
distKm=distMillas/0.6214

horasTot=(segTot/3600)
velPromKMH=(distKm/horasTot)

print("Mi velocidad promedio fue", velPromKMH,"km/h")

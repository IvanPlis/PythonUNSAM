"""
Considere una fila con n personas una al lado de la otra.

Las personas pueden estar infectadas con un virus, ser inmunes o ser suceptibles de enfermarse. Re-
presentaremos esta situacion con una lista L de longitud n que en cada posicíon tiene un 0 (inmune), un 1
(suceptible de enfermarse) o un −1 (tiene el virus). Este virus se propaga inmediatamente a toda persona
suceptible de enfermarse que tenga a alguien enfermo a su lado. Las personas inmunes, no se enferman.
Escriba una funcíon llamada propagar que reciba un vector con ceros, unos y menos unos y devuelva
un vector en el que los menos unos se propagaron a sus vecion con uno.
"""

def propagar (personas):

    for i in range (len(personas)-1):
        if personas[i]==-1:
            if personas[i+1]==1 and i<len(personas):
                personas[i+1]=-1
            if personas[i-1]==1 and i>0:
                personas[i-1]=-1
    return personas

personas=[1,-1, 1, 0, -1, 1, 1, 1, 0, 1, -1, 1, 1]
print(personas)
print(propagar(personas))
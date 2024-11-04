liste = [22, 4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(liste)
nombres_arrondis = [round(nombre) for nombre in liste]
print(nombres_arrondis)
nombres_arrondis.sort()
print(nombres_arrondis)
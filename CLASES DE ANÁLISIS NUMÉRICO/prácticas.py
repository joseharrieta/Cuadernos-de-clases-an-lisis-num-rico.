#ciclo for



vueltas= list(range(1,65))

costal = 0

for vuelta in vueltas:
    granos_por_posición = 2**(vuelta-1)
    granos_totales = costal + granos_por_posición


print(granos_totales)   
    
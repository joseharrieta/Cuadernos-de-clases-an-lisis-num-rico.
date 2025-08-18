ingreso = 11000

if ingreso > 10000:
    print('estás super bien economicamente')
elif ingreso > 1000:
    print('estás bien economicamente')
else:
    print('estás llevado')

    
#if anidados y else if (elif)

sueldo = 100000
gasto = 50000

if sueldo > 80000:
    if sueldo - gasto < 0:
        print('estás en dificít')
    elif sueldo - gasto > 20000:
         print ('vas bien')
    else:
        print('hay que ver si te alcanza')  
        
elif sueldo > 50000:
    print('estás bien en latam')
    
elif sueldo > 20000:
    print('estás bien en colombia')
    
elif sueldo > 10000:
    print('estás bien en venezuela')
    
else:
    print('estás barro')
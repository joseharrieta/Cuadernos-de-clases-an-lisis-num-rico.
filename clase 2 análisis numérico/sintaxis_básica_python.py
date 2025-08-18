#crear una variable
número_pi = 3.1415926535

#acceder a la variable guardada
número_pi

#crear una variable tipo int
n = 50

#acceder a la variable n
n

#verificar tipo de variable
type(n)

#crear una variable decimal (Float)
estatura = 1.65

#acceder a la variable estatura
estatura

#utilizar función type para saber el tipo de variable estatura
type(estatura)

#ciclo "para"...for

posiciones = list(range(1,65))

costal = 0
for posicion in posiciones:
    número_granos_trigo_por_casilla = 2**(posicion-1)
    costal = costal + número_granos_trigo_por_casilla
    
print(costal)

**¿Por qué el profe Marco dice que el método de Neewton falla si lo ponen a buscar un cero donde la funcion solo toca y no atraviesa?**

**¿Cuál es la necesidad del método numérico de Newton?**

**Funciones que se puede encontrar ceros o raices de manera algebraica:**
- funciones lineales
- funciones cuadráticas

**problemas donde el método algebraico es limitado**
- funciones de grado 3 y 4

**problemas donde el método algebraico no puede**
- funciones de grado 5, en adelante.
cuando el modelo sea una función polinomica de grado 5 o más.


supongamos de nuevo el lanzamiento de una pelota (lanzamiento de proyectil o tiro parabolico) con:

. velocidad inicial Vo,
.Ángulo x
. resistencia del aire proporcional a la velocidad (modelo lineal:fuerza de arrastre -kv)


ecuaciones del movimiento:

en direccion vertical, la velocidad satisface la eciacion diferencial:

m (dv/dt) = -mg - kv

donde:

. v = velocidad 
. m = masa proyectil
. g = gravedad, asceleración debida a la atracción gravitatoria
. k = coeficiente de resistencia. 

Fuerza de oposición es proporcional a la velocidad

F= kv

**la velocidad siempre decrece, lo que puede crecer es la rapidez**



la solucion de esa ecuacion lleva a una posicion vertical

h(t) = m/k (vo sin(x))... falta



no existe una formula cerrada para resolver $h(t) = 0$


deduzcamos juntos la formula de newton

1) primero grafico funcion con ejes 
2) altura y tiempo de vuelo
3) tomo (proponer un punto inicial) un to a la izquierda de donde termina el vuelo, tv, en este caso porque la funcion estudiada tiene un dominio cerrado
4) halla el punto (to, h(to)) del grafico de la funcion h
5) halla la ecuacion de la recta tangente
6) halla el cero de esa ecuacion tangente
6) y a ese lo llama t1
7) vuelvo al paso 4, hallo el punto (t1, h(t1))
8) halla la ecuacion de la recta tangente
9) halla el cero de la ecuacion tangente
10) y a ese lo llamo t2




1) hallamos la formula y= h(t)
2) doy una estimacion al cero que denoto por t0
3) m = h'(t0)
punto = (t0, h(t0))

y-y1 = m(x-x1)

t se vuelve t1
h se vuelve 0

h- h(t0) = h' (t0) (t-t0)

0 - h(t0 = h´(t0) (t1-t0)

-h(t0) = h'(t0) (t1-t0)

-h(t0)/h'(t0)= t1-t0

t1 = t0 - h(t0)/ h'(t0)


**nota: cuando un modelo matemático tiene en cuenta mas variables de la realidad es que es necesario métodos numéricos**

**CON CALCULADORA**

parametros fisicos:

. v0 = 20 velocidad inicial
. thetha = pi/4 ángulo de lanzamiento (rad)
. m = 0.15 masa (kg)
. k = 0.1 coeficiente de resistencia (kg/s)
. g = 10 gravedad (m/s^2)

modelo:
  
h(t) = 


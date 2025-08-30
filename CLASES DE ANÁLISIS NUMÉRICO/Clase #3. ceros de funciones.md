**Diseño de Clase: Ceros de funciones**

*Ejemplo: f(x) = 2x+1*

# f(-1) = 2(-1/2)+1
# f(-1) = -1+1
# f(-1) = 0

**ejemplo 3: una parábola con dos ceros**
•	Si antes del cero de la función era positiva, se vuelve negativa y viceversa.

**Ejemplo 4: una parábola con un solo cero**
•	Tanto antes como después del cero de la función es positivo

**Ejemplo 5: una parábola con ningún cero**
•	No existe cero y siempre es negativa o siempre positiva

**Ejemplo 6**

Sea y=f(x)=-(x-22)**2+2, Una función definida en R.

Determinemos juntos c tal que f(c)=0
(es decir, determinemos los ceros o raíces de f)

**Solución**

f(c)=0

-(c-22)**2 + 2 = 0 

Nota: Hallar "ceros" es hallar soluciones de ecuaciones (en este caso cuadrática)


**Representación estándar de función cuadrática:**

y= f(x) = ax^2 +bx + c

**forma canónica:**

y= f(x) = a(x-h)^2 + k


**Situacion problema:**

Se lanza verticalmente un marcador con una velocidad inicial de 1m/s desde una altura h_0 = 1m. Determine el tiempo en que el marcador tarda en llegar al suelo.
**Solución**
"Somos Galileo Galiley (Padre de la experimentación científica)"

g = -9.8 m/s**2 = dv / dt (La aceleración es la derivada de la velocidad con respecto al tiempo)

-10 = dv / dt
integramos para saber cual es la funcion v(t):

v(t) = -10t + c
v(0) = -10(0) + c
v(0) = c = 1

Pero v = dh/ dt
Integramos y hallamos la funcion de la altura h(t):

h(t) = -10t**2/2 + t + c_1
h(t) = -5t**2/2 + t + c_1
h(0) = -5(0)**2 + 0 + c_1
h(t) = -5t**2 + t + 1

Como queremos hallar el tiempo cuando toca el suelo, entonces reemplazamos h(t) = 0, por lo tanto, tenemos que:
0 = -5t**2 + t + 1

Resolvemos la ecuación cuadrática y obtenemos:
t = 0.5585

**notas:**

•	funciones cuadráticas y lineales si se puede de manera algebraica. 
•	funciones trigonométricas y polinómicas se resuelven con métodos numéricos cuando de manera algebraica no se puede
•   importante saber cuando converge y cuando diverge el método de Newton





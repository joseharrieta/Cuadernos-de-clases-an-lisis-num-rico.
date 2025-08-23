#Listas
#almacena diferentes tipos de datos (matriz)
lista = ["Eliecer", 28, "licenciatura en matemáticas", "universidad antioquia"]

print(lista)
print(lista[0])
print(lista[1]) #mostrar lo que hay en esa posición. Empieza desde el cero.

#Tuplas

tupla = ("Eliecer", 28, "licenciatura en matemáticas", "universidad antioquia")
print(tupla[0])
print(tupla[3]) #mismo que la lista, solo que las TUPLAS, NO SE PUEDEN MODIFICAR.


#para verificar cambiemos la lista e intentemos la tupla.

lista[1] = 25

#esto es válido
print(lista[1]) 

#esto no es válido
#tupla[1] = 25


#El conjunto set

#creando un conjunto set

set = {"Eliecer", 28, "licenciatura en matemáticas", "universidad antioquia"}

#no se puede ver elemento segun posición de un conjunto set

#print(set[0])

#no puede cambiar un elemento del conjunto set
#set[0] = "josé"

#si se puede redefinir todo el conjunto set

set= {"josé", 27, "lic en matemáticas", "udea"}
print(set)

#diccionario (dict)

diccionario = {
    'nombre': "Eliecer",
    'edad' : "28",
    'carrera' : "lic en matemáticas",
    'universidad': "udea"
}

print(diccionario['nombre'])

print(diccionario['edad'])
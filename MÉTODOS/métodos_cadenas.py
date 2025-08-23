cadena1 = "Hola, soy, Eliecer"
cadena2 = "Bienvenido José"

#convierte a mayusculas

mayusc = cadena1.upper()

#convierte a minusculas

minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayuscula = cadena1.capitalize()

print(mayusc)
print(minusc)
print(primer_letra_mayuscula)

#busqueda de una cadena en otra cadena/ si no hay coincidencias devuelve -1

busqueda_find = cadena1.find("d")

print(busqueda_find)

#busqueda de una cadena en otra cadena

busqueda_index = cadena1.index("H")

print(busqueda_index)

#si es numérico devuelve True, sino False

es_numérico = cadena1.isnumeric()

print(es_numérico)

#si es alfanumérico devuelve True, sino False

es_alfanumérico = cadena1.isalpha()
print(es_numérico)

#contamos las coincidencias  de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias.

contar_coincidencia = cadena1.count("a")

print(contar_coincidencia)

#contamos cuántos caracteres tiene una cadena

contar_caracteres = len(cadena1)

print(contar_caracteres)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True

empieza_con = cadena1.startswith("H")

print(empieza_con)


#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True

termina_con = cadena1.endswith("H")

print(termina_con)


#reemplaza un pedazo de la cadena dada por otra dada

cadena_nueva = cadena1.replace("Hola", "Holu maquina")

print(cadena_nueva)



#separar cadenas con la cadena que le pasemos

cadena_separada = cadena1.split(",")

print(cadena_separada)

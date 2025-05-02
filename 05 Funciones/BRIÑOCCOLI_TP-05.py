#1) Crear una lista con los numeros del 1 al 100 que sean  ultiplos de 4. Utilizar la funcion ranger.
multiplosde_4 = list(range(4, 101, 4))

print(multiplosde_4)

#2) Crear una lista con cinco elementos (colocar los elementos que mas te gusten y mostrar el penultimo).

mis_favoritos = ["Explorar", "Aprender", "Viajar", "Comer", "Cocinar"]

penultimo_elemento = mis_favoritos[-2]
print(f"Mi lista de favoritos es: {mis_favoritos}")
print(f"El penultimo elemento de la lista es: {penultimo_elemento}")

#3) Crear una lista vacia, agregar tres palabras con append e imprmir la lista resultante por pantalla.

mi_lista = []
mi_lista.append("Hola")
mi_lista.append("Como estás")
mi_lista.append("Que tengas un buen día")

print(mi_lista)

#4) Reemplazar el segundo y ultimo valor de las lista "animales" con las palabras "loro" y "oso", respectivamente. Imprimir la lista por pantalla.

animales = ["perro", "gato", "elefante", "jirafa", "tigre"]
animales[1] = "loro" #reemplaza el segundo elemento (indice 1) con "loro"
animales[-1] = "oso" #reemplaza el ultimo elemento (indice -1) con "oso"
print(animales)

#5) Analiza el siguiente programa y explica con tus palabras que es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros) 

#En la primera linea se crea una lista con el nombre "numeros" y este tiene los numeros 8, 15, 3, 22 y 7, es la segunda linea.
#se utiliza la funcion "remove" para eliminar el numero mas grande que tenemos en la lista, que es el 22. Y por ultimo se imprime la lista sin el 22.

#6) Crear una lista con numeros del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

mi_lista = list(range(10, 31, 5))
print(mi_lista[:2])

#7) Reemplazar los dos valores centrales (indices 1 y 2) de la lista "autos" por dos nuevos valores cualesquiers.

autos =["sedan", "polo", "suran", "gol"]
autos[1] = "peugeot" 
autos[2] = "chevrolet_onix" 
print(autos)

#8) Crear una lista vacia llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista por pantalla.
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9) Dada la lista "compras", cuyo elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa" ], ["agua" ]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla.

compras[2].append("jugo") # Agregar "jugo" a la lista del tercer cliente
indice_fideos = compras[1].index("fideos") # Obtener el índice de "fideos" en la lista del segundo cliente
compras[1][indice_fideos] = "tallarines" # Reemplazar "fideos" por "tallarines"

compras[0].remove("pan") # Eliminar "pan" de la lista del primer cliente

print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#Posición lista_anidada[0]: 15
#Posición lista_anidada[1]: True
#Posición lista_anidada[2][0]: 25.5
#Posición lista_anidada[2][1]: 57.9
#Posición lista_anidada[2][2]: 30.6
#Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

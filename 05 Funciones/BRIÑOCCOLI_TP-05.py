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

#6) Reemplazar lso dos valores centrales (indices 1 y 2) de la lista "autos" por dos nuevos valores cualesquiers.

autos =["sedan", "polo", "suran", "gol"]
autos[1] = "peugeot" 
autos[2] = "chevrolet_onix" 
print(autos)


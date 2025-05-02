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
#6) Ejercicio N°6

import random
from statistics import mode, median, mean

lista_numeros = [random.randint(1, 100) for i in range (100)]

moda = mode(lista_numeros)
mediana = median(lista_numeros)
media = mean(lista_numeros)

print( '\n',moda,'\n' ,mediana,'\n',media,'\n')

#Sesgo posituivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.
if media > mediana and mediana > moda:
    print(" Sesgo Positivo ")
    #Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
elif media < mediana and mediana < moda:
    print(" Sesgo negativo ")
    #Sin Sesgo: Cuando la media, la mediana y la moda son iguales.
elif media == mediana and mediana == moda:
    print(" Sin Sesgo ")

else:
    print(" UPPS! Error")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla;}
# en caso contrario, dejar el string tal cual lo ingreso el usuario e imprimirlo por pantalla.

cadena = str(" Ingresa una frase o palabra ")
vocales = ["a", "e", "i", "o", "u"]
if cadena[-1:].lower()in vocales:
    print(f"[cadena]!")
else:
    print(f" cadena")

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el numero 1, 2 o 3 dependiendo de la opción que desee:
# *1) Si quiere su nombre en mayuscula.
# *2) Si quiere su nombre en minuscula.
# *3) Si quiere su nombre con la primera letra mayuscula.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombre = str(input)
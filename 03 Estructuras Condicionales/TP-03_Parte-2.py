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

nombre = str(input(" Ingrese por favor su nombre "))
opc = int(input('''Como quieres que escriba tu nombre? 
                1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
                2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
                3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.'''))

if opc == 1:
    print(f' Hola {nombre.upper()}!')
elif opc == 2:
    print(f'hola {nombre.lower()}!')
elif opc == 3:
    print(f'Hola {nombre.title()}!')

#9) Escribir un Programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorias segun la escala de
# Richter e imprima el resultado por pantalla:

magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3.0:
    print("Muy leve (imperceptible)")
elif magnitud >= 3.0 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")

#10) Ejercicio N°10= Estaciones del Año

hemisferio = input("Ingrese el hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio not in ["N", "S"] or mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Datos inválidos. Asegúrese de ingresar un hemisferio válido (N/S) y una fecha correcta.")
else:
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
    elif hemisferio == "S":
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
    
    print(f"La estación en su ubicación es: {estacion}")
    
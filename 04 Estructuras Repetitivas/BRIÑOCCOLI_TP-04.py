# Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un numero por linea.

for i in range(1,101):
    print(i, '\t')

#2) Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene

numero = int(input(" Ingrese un numero entero: "))
contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
            numero //= 10
            contador += 1

print(" Cantidad de digitos", contador)

#3) Escribe un programa que sume todos los numeros enteros comprendidos entre dos valores dados por el usuario,
# excluyendo esos dos valores.

limite_1 = int(input(" Ingrese por favor un numero entero"))
limite_2 = int(input(" Ingrese un segundo numero entero "))

for i in range(limite_1 + 1, limite_2):
     print(i)

#4) Elabora un programa que permita al usuario ingresar numeros enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado
# cuando el usuario ingrese un 0.

num = int(input(" Ingrese un numero: "))
sumador = 0

while num != 0:
     sumador += num
     print(" Total parcial ", sumador)
     num = int(input(" Ingrese un numero: "))

print(" Total acumulado:", sumador)

#5) Crea un juego en el que el usuario deba adivinar un numero aleatorio entre 0 y 9. Al final,
# el programa debe mostrar cuantos intentos fueron necesarios para acertar el número.

import random
num_aleatorio = random.randint(0, 9)

num_user = int(input(" Intenta adivinar el numero: "))
intentos = 0

while num_user != num_aleatorio:
    num_user = int(input(" Intenta de nuevo "))
    intentos += 1

print(f" Felicitaciones! Acertaste, Te llevo  {intentos} intentos/s")

#6) Desarrolla un programa que imprima en pantalla todos los numeros pares comprendidos entre 0 y 100, en orden decreciente.

for num in range(0+2, 101, 2):
     print(num)

#7) Crea un programa que calcule la suma de todos los numeros comprendidos entre 0 y un numero entero positivo indicado por el usuario.

numero = int(input(" Ingrese, por favor un numero positivo "))
suma = 0

for i in range(0, numero +1):
     suma += i

print(f" La suma total es de {suma} ")

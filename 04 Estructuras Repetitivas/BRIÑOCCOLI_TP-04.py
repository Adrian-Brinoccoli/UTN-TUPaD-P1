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

#TrabajoPractico N1
#Ejercicio N°1
print("Hola Mundo!")

#Ejercicio N°2
nombre = input("Por favor ingrese su nombre")
print(f"Hola {nombre}!")

#Ejercicio N°3
nombre = input("Por favor ingrese su nombre")
apellido = input("Por favor ingrese su apellido")
edad = input("Por favor ingrese su edad")
lugar_de_residencia = input("Por favor ingrese su domicilio")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

#Ejercicio N°4 Crea un programa que pida al usuario el radio de un circulo e imprima por pantalla su área y su perímetro.
import math

radio = float(input("Introduce el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

#Ejercicio N°5 Crea un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuantas horas equivale.
segundos = int(input("Introduce la cantidad de segundos: "))
horas = segundos // 3600

print(f"{segundos} segundos equivalen a {horas} horas")

#Ejercicio N°6 Crea un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Ejercicio N°7 Crea un programa que pida al usuario dos numeros enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Introduce el primer número"))
numero2 = int(input("Introduce el segundo número"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Resultado de sumar: {numero1} + {numero2} = {suma}")
print(f"Resultado de restar: {numero1} - {numero2} = {resta}")
print(f"Resultado de multiplicar: {numero1} * {numero2} = {multiplicacion}")
print(f"Resultado de dividir: {numero1} / {numero2} = {division}")

#Ejercicio N°8 Crea un Programa que pida al usuario su altura y su peso e imprima por pantalla su índece de masa corporal.
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

#Ejercicio N°9 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")

#Ejercicio N°10 Crear un programa que pida al usuario 3 numeros e imprima por pantalla el promedio de dichos números.
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")
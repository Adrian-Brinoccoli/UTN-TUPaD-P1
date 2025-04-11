#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga " Es mayor de Edad "

edad = int(input(" Ingresa tu edad: "))

if edad >= 18:
    print(" Sos mayor de edad ")
else:
    print(" No sos mayor de Edad ")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga "Aprobado"; 
# en caso contrario deberá mostrar el mensaje "Desaprobado"

nota = int(input(" Ingresa tu nota: "))
if nota >= 6:
    print(" Felicidades has Aprobado ")
else:
    print(" Suerte para la proxima, no Aprobaste")

#3) Escribir un programa que permita ingresar solo numeros pares. Si el usuario ingresa un
# numero par, imprimir por pantalla "Ha ingresado un numero par"; en caso contrario,
# imprimir por pantalla " Por favor, ingrese un numero impar"

num = int(input(" Ingrese un numero par: "))

if num % 2 == 0:
    print(" Has ingresado un numero par ")
else:
    print(" Incorrecto, Por favor ingresa un numero par:")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cual de las siguientes categorias pertenece:
# Niño/a: menor a 12 años
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/ a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años

edad = int(input(" Ingresa tu edad:"))

if edad <12:
    print(" Niño/a")
elif edad >= 12 and edad < 18:
    print(" Adolescente ")
elif edad >= 18 and edad < 30:
    print(" Adulto/a Joven: ")
elif edad >= 30:
    print(" Adulto ")
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga " Es mayor de Edad "

edad = int(input(" Ingresa tu edad: "))

if edad >= 18:
    print(" Sos mayor de edad ")
else:
    print(" No sos mayor de Edad ")

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga "Aprobado"; 
# en caso contrario deberá mostrar el mensaje "Desaprobado"

nota = int(input(" Ingresa tu nota: "))
if nota >= 6:
    print(" Felicidades has Aprobado ")
else:
    print(" Suerte para la proxima, no Aprobaste")


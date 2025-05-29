#1) Crear una funcion llamada imprimir_hola_mundo que imprima por pantalla el mensaje: "Hola Mundo".

def imprimir_hola_mundo():
    print("Hola Mundo")

# Llamada a la funcion desde el programa principal

if __name__ == "__main__":
    imprimir_hola_mundo()

#2) Crea una funcion llamada saludar_usuario(nombre) que reciba como parametro un nombre y devuelva un saludo personalizado.
# Por ejemplo si se llama con saludar_usuario("Marcos") debera devolver "Hola Marcos". LLamar a esta funcion desde el programa principal
# solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}"

# Llamada a la funcion desde el programa principal

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre)
    print(saludo)

#3) Crear una funcion llamada informacion_personal (nombre, apellido, edad, residencia) que reciba cuatro parametros e imprima: "Soy [nombre][apellido],
# tengo [edad] años y vivo en [residencia]". Pedir los datos al usuario y llamar a esta funcion con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Llamada a la funcion desde el programa principal

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parametro y devuelva el area del circulo.
# calcular_perimetro_circulo(radio) que reciba el radio como parametro y devuelva el perimitro del circulo.
# solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar el radio al usuario

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del circulo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El area del circulo es: {area}")
    print(f"El perimetro del circulo es: {perimetro}")

#5) Crear una funcion llamadas segundos _a_horas(segundos) que reciba una cantidad de segundos como parametros y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta funcion.

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos"

# Programa Principal-

if __name__ == "__main__":
    segundos = int(input("Ingrese la cantidad de segundos: "))
    resultado = segundos_a_horas(segundos)
    print(f"Equivalente a: {resultado}")      

#6) Crear una funcion llamada tabla_multiplicar(numero) que reciba un numero como parametro y imprima la tabla de multiplicar de ese numero del 1 al 10.
# Pedir al usuario el numero y llamar a la funcion.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}") 

# Programa Principal

if __name__ == "__main__":
    numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

#7) Crear una funcion llamda operaciones_basicas(a,b) que reciba dos numeros como parametros y devuelva una tupla con los resultados de sumarlos, restarlos, multiplicarlos.
# y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: Division por cero"
    return (suma, resta, multiplicacion, division)

# Programa Principal

if __name__ == "__main__":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    resultados = operaciones_basicas(a, b)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicacion: {resultados[2]}")
    print(f"Division: {resultados[3]}")

#8) Craer una funcion llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el indice de masa corporal
# (IMC). Solicita al usuario los datos y llamar a la funcion para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    if altura <= 0:
        return "Error: La altura debe ser mayor que cero."
    imc = peso / (altura ** 2)
    return round(imc, 2)

# Programa Principal

if __name__ == "__main__":
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su indice de masa corporal (IMC) es: {imc}")

#9) Crear una funcion llamada celcius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir
# al usuario la temperatura en Celsius y mostrar el resultado usando la funcion.

def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)

# Programa Principal

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celcius_a_fahrenheit(celsius)
    print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")

#10) Crear una funcion llamada calcular_promedio(a, b, c) que reciba tres numeros como parametros y devuelva el promedio de ellos.
# Solicitar los numeros al usuario y mostrar el resultado usando esta funcion.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3 

# Programa Principal

if __name__ == "__main__":
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    c = float(input("Ingrese el tercer numero: "))
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio de los numeros es: {promedio}") 
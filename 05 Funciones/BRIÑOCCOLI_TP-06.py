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


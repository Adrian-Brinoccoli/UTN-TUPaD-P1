#1) Crea una funcion recursiva que calcule el factorial de un numuero. Luego, utiliza esa funcion para calcular y mostrar en pantalla el factorial de todos
# los numeros enteros entre 1 y el numero que indique el usuario.

def factrorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factrorial_recursivo(n - 1)
    
#Parte del programa
if __name__ == "__main__":
    while True:
        try:
            num_usuario = int(input("Ingrese un numero entero positivo para calcularlo: "))
            if num_usuario < 0:
                print("Por favor, ingrese un numero entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero. ")

    print(f"\nCalculando factoriales hasta {num_usuario}:")
    for i in range(1, num_usuario + 1):
        print(f"El factorial de {i} es {factrorial_recursivo(i)}")

#2) Crea una funcion recursiva que calcule el valor de la serie de Fibonacci en la posicion indicada. Posteriormente, muestra
# la serie completa hasta la posicion que el usuario especifique.
def fibonacci_recursivo(pos):

    if pos == 0:
        return 0
    # F(1) = 1
    elif pos == 1:
        return 1
    # Caso recursivo: F(pos) = F(pos-1) + F(pos-2)
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

# --- Parte principal del programa ---
if __name__ == "__main__":
    while True:
        try:
            num_posiciones = int(input("Ingresa la cantidad de posiciones de la serie de Fibonacci a mostrar: "))
            if num_posiciones < 0:
                print("Por favor, ingresa un número positivo. ")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    print(f"\nSerie de Fibonacci hasta la posición {num_posiciones}:")
    for i in range(num_posiciones + 1): # Incluimos la posición 0 hasta la posición indicada
        valor_fib = fibonacci_recursivo(i)
        print(f"F({i}) = {valor_fib}")

#3) Crea una funcion recursiva que calcule la potencia de un numero base elevado a un exponent, utilizando la formula 𝑛𝑚= 𝑛∗𝑛(𝑚−1).
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return "Error: Exponente negativo no soportado directamente por esta implementación recursiva."
    else:
        return base * potencia_recursiva(base, exponente - 1)

# Programa Principal:
if __name__ == "__main__":
    print("Calculadora de Potencia Recursiva" )

    while True:
        try:
            base_input = float(input("Ingresa la base: "))
            exponente_input = int(input("Ingresa el exponente (positivo): "))

            if exponente_input < 0:
                print("Por favor, ingresa un exponente entero no negativo para esta función.")
                continue 
            break
        except ValueError:
            print("Entrada inválida. Por favor, asegúrate de ingresar números válidos.")

    resultado = potencia_recursiva(base_input, exponente_input)

    print(f"\nEl resultado de {base_input} elevado a la {exponente_input} es: {resultado}")

#4) Crea una funcion recursiva en Python que reciba un numero entero positivo en base ddecimal
# y devuelva su representacion en binario como una cadena de texto.
def decimal_a_binario_recursivo(decimal_num):
    if decimal_num == 0:
        return "0"
    elif decimal_num < 0:
        return "Error: La función solo acepta números enteros positivos."
    else:
        # Calculamos el residuo (el bit menos significativo actual)
        residuo = decimal_num % 2
        # Calculamos la parte entera de la división (el resto del número a convertir)
        cociente = decimal_num // 2
        if cociente == 0:
            return str(residuo)
        # Si el cociente no es 0, continuamos la recursión
        else:
            return decimal_a_binario_recursivo(cociente) + str(residuo)

# --- Algoritmo General para Prueba ---
if __name__ == "__main__":
    print("--- Convertidor Decimal a Binario Recursivo ---")
    while True:
        try:
            num_decimal = int(input("Ingresa un número entero positivo: "))
            if num_decimal < 0:
                print("Por favor, ingresa un número entero positivo (o 0).")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    binario_result = decimal_a_binario_recursivo(num_decimal)

    print(f"\nEl número decimal {num_decimal} en binario es: {binario_result}")

#5) implementa una funcion recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva
# True si es un palindromo o False si no lo es.
    #Requisitos: la solicion debe ser recursiva, no se debe usar [::-1] ni la funcion reversed().
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 caracteres, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Comparamos el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva eliminando el primer y último carácter
    return es_palindromo(palabra[1:-1])

#Programa Principal:
if __name__ == "__main__":
    print("Verificador de Palíndromos" )
    while True:
        palabra = input("Ingresa una palabra o frase (sin espacios ni tildes): ").replace(" ", "").lower()
        if not palabra.isalpha():
            print("Por favor, ingresa solo letras sin espacios ni tildes.")
            continue
        break

    resultado = es_palindromo(palabra)
    if resultado:
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

#6) Escribir una funcion recursiva en Python llamada suma_digitos(n) que reciba un numero entero positivo y devuelva la suma de todos sus digitos.
    #Restricciones: no se puede convertir el numero a string. Usá operaciones matematicas (%, //) y recursion.
def suma_digitos(n):
    # Caso base: si n es 0, la suma de los dígitos es 0
    if n == 0:
        return 0
    else:
        # Sumar el último dígito (n % 10) y llamar recursivamente con el resto del número (n // 10)
        return (n % 10) + suma_digitos(n // 10)
# Programa Principal:
if __name__ == "__main__":
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo: "))
            if numero < 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    resultado_suma = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado_suma}")

#7) Un niño esta construyendo una piramide de bloques. En el nivel mas bajo coloca N bloques, en el siguiente nivel uno menos (n-1), y asi 
# sucesivamente hasta llegar al ultimo nivel con un solo bloque.
    #Escribir una funcion recursiva contar_bloques(n) que reciba el numero de bloques en el nivel mas bajo y devuelva el total de bloques que necesita
    # para construir toda la piramide.

def contar_bloques(n):
    # Caso base: si n es 0, no hay bloques
    if n == 0:
        return 0
    # Caso recursivo: sumar el bloque actual (n) y los bloques del nivel siguiente (n-1)
    else:
        return n + contar_bloques(n - 1)

# Programa Principal:
if __name__ == "__main__":
    while True:
        try:
            bloques = int(input("Ingresa el número de bloques en el nivel más bajo: "))
            if bloques < 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    total_bloques = contar_bloques(bloques)
    print(f"Total de bloques necesarios para construir la pirámide: {total_bloques}")

#8) Escribir una funcion recursiva llamada contar_digitos(numeros, digito) que reciba un numero entero positivo (numero) y un digito (entre 0 y 9)
# y devuelva cuantas veces aparece ese digito dentro del numero.
def contar_digitos(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito del número es igual al dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digitos(numero // 10, digito)
        else:
            return contar_digitos(numero // 10, digito) 
# Programa Principal:
if __name__ == "__main__":
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo: "))
            if numero < 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    while True:
        try:
            digito = int(input("Ingresa un dígito (entre 0 y 9): "))
            if digito < 0 or digito > 9:
                print("Por favor, ingresa un dígito válido entre 0 y 9.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un dígito entre 0 y 9.")

    cantidad_digitos = contar_digitos(numero, digito)
    print(f"El dígito {digito} aparece {cantidad_digitos} veces en el número {numero}.")




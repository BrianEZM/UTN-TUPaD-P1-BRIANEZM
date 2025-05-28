# Declaracion de Funciones:
def numero_de_ejercicio(ejercicio):
    return print(f"\nEjercicio N°: {ejercicio}")


def iterar_funcion(cant, funcion_a_iterar):
    for i in range(0, cant + 1):
        resultado = funcion_a_iterar(i)
        print(f"El {funcion_a_iterar.__name__} de {i} es: {resultado}")


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(num):
    if num == 0:
        return 0
    else:
        return 1 if num == 1 else fibonacci(num - 1) + fibonacci(num - 2)


def calcular_potencia_recursiva(base, exponente):
    if exponente < 0:
        return "Error: El exponente debe ser un número entero positivo."
    elif exponente == 0:
        return 1
    else:
        return base * calcular_potencia_recursiva(base, exponente - 1)


def decimal_a_binario_recursivo(numero_decimal):
    if numero_decimal < 0:
        return "Error: El número debe ser un entero positivo."
    elif numero_decimal == 0:
        return "0"
    elif numero_decimal == 1:
        return "1"
    else:
        parte_izquierda = decimal_a_binario_recursivo(numero_decimal // 2)
        parte_derecha = str(numero_decimal % 2)
        return parte_izquierda + parte_derecha


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True

    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False


def suma_digitos(n):
    if not isinstance(n, int):
        return "Error: La entrada debe ser un número entero."
    if n < 0:
        return "Error: La entrada debe ser un número entero positivo."
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)


def contar_bloques(n):
    if not isinstance(n, int):
        return "Error: El número de bloques debe ser un entero."
    if n <= 0:
        return "Error: El número de bloques en el nivel más bajo debe ser un entero positivo."

    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


def contar_digito(numero, digito):
    if not isinstance(numero, int) or not isinstance(digito, int):
        return "Error: Ambos argumentos deben ser números enteros."
    if numero < 0:
        return "Error: El número debe ser un entero positivo."
    if not (0 <= digito <= 9):
        return "Error: El dígito a buscar debe estar entre 0 y 9."

    if numero == 0:
        return 0

    conteo_actual = 0
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        conteo_actual = 1
    return conteo_actual + contar_digito(numero // 10, digito)


# Programa principal:
numero_de_ejercicio(1)
num_hasta_factorizar = int(input("Ingrese un numero entero: "))
iterar_funcion(num_hasta_factorizar, factorial)

numero_de_ejercicio(2)
num_hasta_fibonacci = int(input("Ingrese un numero entero: "))
iterar_funcion(num_hasta_fibonacci, fibonacci)

numero_de_ejercicio(3)
base_usuario = float(input("Introduce la base (número real): "))
exponente_usuario = int(input("Introduce el exponente (entero no negativo): "))
resultado_potencia = calcular_potencia_recursiva(base_usuario, exponente_usuario)
print(f"{base_usuario} elevado a la potencia de {exponente_usuario} es: {resultado_potencia}")

numero_de_ejercicio(4)
num_a_binario = int(input("Ingrese un numero entero: "))
print(decimal_a_binario_recursivo(num_a_binario))

numero_de_ejercicio(5)
palabra_usuario = input("Ingresa una palabra (sin espacios ni tildes): ").lower()
print(f"'{palabra_usuario}' es un palíndromo? {es_palindromo(palabra_usuario)}")

numero_de_ejercicio(6)
num_sum_usuario = int(input("Ingresa un número entero positivo: "))
resultado = suma_digitos(num_sum_usuario)
print(f"La suma de los dígitos de {num_sum_usuario} es: {resultado}")

numero_de_ejercicio(7)
bloques_usuario = int(input("Ingresa el número de bloques en el nivel más bajo (entero positivo): "))
resultado = contar_bloques(bloques_usuario)
print(f"Para un nivel más bajo de {bloques_usuario} bloques, el total de bloques necesarios es: {resultado}")

numero_de_ejercicio(8)
numero_usuario = int(input("Ingresa el número entero positivo: "))
digito_usuario = int(input("Ingresa el dígito a buscar (0-9): "))
resultado = contar_digito(numero_usuario, digito_usuario)
print(f"El dígito {digito_usuario} aparece {resultado} vez(veces) en el número {numero_usuario}.")

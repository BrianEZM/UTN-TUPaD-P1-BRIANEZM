# Declaracion de Funciones:
def numero_de_ejercicio(ejercicio):
    return print(f"\nEjercicio N°: {ejercicio}")


def imprimir_hola_mundo(mensaje):
    return print(f"Este es el mensaje recibido: {mensaje}")


def saludar_usuario(usuario):
    return print(f"Hola {usuario}")


def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")


def validar_entrada(mensaje, min=float("-inf"), max=float("inf")):
    while True:
        try:
            entrada_usuario = float(input(mensaje))
            if entrada_usuario < min:
                print(f"Error. Inténtalo de nuevo. {mensaje}")
            elif entrada_usuario > max:
                print(f"Error. Inténtalo de nuevo. {mensaje}")
            else:
                break
        except ValueError:
            print(f"Error. Inténtalo de nuevo. {mensaje}")
    return entrada_usuario


def calcular_area_circulo(radio):
    return print(f"El area es {3.14159 * radio * radio}")


def calcular_perimetro_circulo(radio):
    return print(f"El perimetro es {2 * 3.14159 * radio}")


def segundos_a_horas(segundos):
    return print(f"{segundos} segundos son {(segundos / 60) / 60} horas.")


def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0:
        division = a / b
    else:
        division = None
        print(f"No se puede dividir por cero para {a} / {b}")

    return print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {multiplicacion}, Division: {division}")


def calcular_imc(peso, altura):
    altura_metros = altura / 100
    return print(f"Tu IMC es: {peso / (altura_metros ** 2)}")


def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")


def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return print(f"El promedio de los tres numeros es {promedio}")


# Programa principal:
numero_de_ejercicio(1)
imprimir_hola_mundo("Hola Mundo! Soy Brian Zapata Marin.")
imprimir_hola_mundo("Hola Mundo! Este es otro mensaje de prueba.")

numero_de_ejercicio(2)
saludar_usuario("Brian")
saludar_usuario("Emanuel")

numero_de_ejercicio(3)
informacion_personal("Brian", "Zapata Marin", 34, "Vistalba,Mendoza")

numero_de_ejercicio(4)
radio_usuario = validar_entrada("Ingrese un radio: ", 1)
calcular_area_circulo(radio_usuario)
calcular_perimetro_circulo(radio_usuario)

numero_de_ejercicio(5)
segundos_usuario = validar_entrada("Ingreses un cantidad de segundos: ", 1)
segundos_a_horas(segundos_usuario)

numero_de_ejercicio(6)
tabla_del = validar_entrada("Ingrese un numero: ", 1)
tabla_multiplicar(tabla_del)

numero_de_ejercicio(7)
primer_num = validar_entrada("Ingrese un numero: ")
segundo_num = validar_entrada("Ingrese un numero (no se puede dividir por cero): ")
operaciones_basicas(primer_num, segundo_num)

numero_de_ejercicio(8)
peso_usuario = validar_entrada("Ingrese su peso (maximo 300kg): ", 1, 300)
altura_usuario = validar_entrada("Ingrese su altura (maximo 300cm): ", 1, 300)
calcular_imc(peso_usuario, altura_usuario)

numero_de_ejercicio(9)
celsius_usuario = validar_entrada("Ingrese una temperatura en Celsius: ")
celsius_a_fahrenheit(celsius_usuario)

numero_de_ejercicio(10)
num1 = validar_entrada("Ingrese un primer numero: ")
num2 = validar_entrada("Ingrese un segundo numero: ")
num3 = validar_entrada("Ingrese un tercer numero: ")
calcular_promedio(num1, num2, num3)

import random, statistics

# Ejercicio 1:
print("EJERCICIO 1: ")
edad_usuario = int(input("Ingrese tu edad: "))

if edad_usuario > 18:
    print("Eres mayor de edad")

# Ejercicio 2:
print("EJERCICIO 2: ")
nota_usuario = float(input("Ingrese su nota: "))

if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3:
print("EJERCICIO 3: ")
input_number = int(input("Ingrese un numero: "))

if input_number % 2 != 0:
    print("El num es impar")
else:
    print("El num es par")

# Ejercicio 4:
print("EJERCICIO 4: ")
edad_ingresada = int(input("Por favor, ingresa tu edad: "))

if edad_ingresada < 12:
    print("Niño/a")
elif edad_ingresada >= 12 and edad_ingresada < 18:
    print("Adolescente")
elif edad_ingresada >= 18 and edad_ingresada < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5:
print("EJERCICIO 5: ")
password_usuario = input("Ingreses una contraseña: ")

if len(password_usuario) < 8 or len(password_usuario) > 14:
    print("Su contraseña es muy corta o muy larga.")
else:
    print("Ha ingresado una contraseña correcta.")

# Ejercicio 6:
print("EJERCICIO 6: ")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
nums_media = statistics.mean(numeros_aleatorios)
nums_moda = statistics.mode(numeros_aleatorios)
nums_mediana = statistics.median(numeros_aleatorios)

print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {nums_moda}")
print(f"Mediana: {nums_mediana}")
print(f"Media: {nums_media}")

if nums_mediana == nums_moda and nums_mediana == nums_media:
    print("No hay sesgo")
elif nums_media > nums_mediana and nums_mediana > nums_moda:
    print("Hay sesgo positivo/a la derecha")
elif nums_media < nums_mediana and nums_mediana < nums_moda:
    print("Hay sesgo negativo/a la izquierda")

# Ejercicio 7:
print("EJERCICIO 7: ")
texto_usuario = input("Ingrese un texto: ")
vocales = "aeiouAEIOU"

if texto_usuario and texto_usuario[-1] in vocales:
    resultado = texto_usuario + "!"
    print(resultado)
else:
    print(texto_usuario)

# Ejercicio 8:
print("EJERCICIO 8: ")
nombre = input("Ingrese su nombre: ")
opcion_usuario = input("Ingrese la opción deseada (1, 2 o 3):\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n")

if opcion_usuario == '1':
    nombre_transformado = nombre.upper()
    print("Su nombre en mayúsculas:", nombre_transformado)
elif opcion_usuario == '2':
    nombre_transformado = nombre.lower()
    print("Su nombre en minúsculas:", nombre_transformado)
elif opcion_usuario == '3':
    nombre_transformado = nombre.title()
    print("Su nombre con la primera letra mayúscula:", nombre_transformado)
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

# Ejercicio 9:
print("EJERCICIO 9: ")
magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

if magnitud < 3:
    categoria = "Muy leve"
elif 3 <= magnitud < 4:
    categoria = "Leve"
elif 4 <= magnitud < 5:
    categoria = "Moderado"
elif 5 <= magnitud < 6:
    categoria = "Fuerte"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte"
else:
    categoria = "Extremo"

print(f"Magnitud: {magnitud} || Categoría: {categoria}")

# Ejercicio 10:
print("EJERCICIO 10: ")
def determinar_estacion(hemisferio, mes, dia):

    mes = mes.lower()
    dia = int(dia)

    if hemisferio.upper() == 'N':
        if (mes == 'diciembre' and dia >= 21) or \
                (mes == 'enero') or \
                (mes == 'febrero') or \
                (mes == 'marzo' and dia <= 20):
            return "Invierno"
        elif (mes == 'marzo' and dia >= 21) or \
                (mes == 'abril') or \
                (mes == 'mayo') or \
                (mes == 'junio' and dia <= 20):
            return "Primavera"
        elif (mes == 'junio' and dia >= 21) or \
                (mes == 'julio') or \
                (mes == 'agosto') or \
                (mes == 'septiembre' and dia <= 20):
            return "Verano"
        elif (mes == 'septiembre' and dia >= 21) or \
                (mes == 'octubre') or \
                (mes == 'noviembre') or \
                (mes == 'diciembre' and dia <= 20):
            return "Otoño"
        else:
            return "Fecha inválida"
    elif hemisferio.upper() == 'S':
        if (mes == 'diciembre' and dia >= 21) or \
                (mes == 'enero') or \
                (mes == 'febrero') or \
                (mes == 'marzo' and dia <= 20):
            return "Verano"
        elif (mes == 'marzo' and dia >= 21) or \
                (mes == 'abril') or \
                (mes == 'mayo') or \
                (mes == 'junio' and dia <= 20):
            return "Otoño"
        elif (mes == 'junio' and dia >= 21) or \
                (mes == 'julio') or \
                (mes == 'agosto') or \
                (mes == 'septiembre' and dia <= 20):
            return "Invierno"
        elif (mes == 'septiembre' and dia >= 21) or \
                (mes == 'octubre') or \
                (mes == 'noviembre') or \
                (mes == 'diciembre' and dia <= 20):
            return "Primavera"
        else:
            return "Fecha inválida"
    else:
        return "Hemisferio inválido. Por favor, ingrese 'N' o 'S'."

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ")
mes = input("¿Qué mes del año es?: ")
dia = input("¿Qué día es?: ")

estacion = determinar_estacion(hemisferio, mes, dia)
print(f"En el hemisferio {hemisferio.upper()}, la estación actual es: {estacion}")
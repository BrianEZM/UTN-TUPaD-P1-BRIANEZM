import random

# Ejercicio 1:
print("EJERCICIO 1: ")
for i in range(101):
    print(i)

# Ejercicio 2:
print("EJERCICIO 2: ")
num_usuario = int(input("Ingrese un número entero: "))
cant_digitos = len(str(num_usuario))
print(f"El número {num_usuario} tiene {cant_digitos} dígitos.")

# Ejercicio 3:
print("EJERCICIO 3: ")
num1_usuario = int(input("Ingrese un número entero: "))
num2_usuario = int(input("Ingrese otro número entero: "))
suma_total = 0

if num1_usuario > num2_usuario:
    num1_usuario, num2_usuario = num2_usuario, num1_usuario

for numero in range(num1_usuario + 1, num2_usuario):
    suma_total += numero

print(f"La suma total es: {suma_total}")

# Ejercicio 4:
print("EJERCICIO 4: ")
total = 0
numero = int(input("Ingrese un número entero para sumar (0 para finalizar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingrese otro número entero para sumar (0 para finalizar): "))

print(f"La suma total es: {total}")

# Ejercicio 5:
print("EJERCICIO 5: ")
num_aleatorio_1_10 = random.randint(0,9)
intento_usuario = int(input("Intenta adivinar el numero entre 0 y 9: "))
intentos = 1

while num_aleatorio_1_10 != intento_usuario:
    intento_usuario = int(input("Intenta nuevamente: "))
    intentos += 1

print(f"Adivinaste! El numero era {num_aleatorio_1_10}. Intentaste {intentos} veces.")

# Ejercicio 6:
print("EJERCICIO 6: ")

for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7:
print("EJERCICIO 7: ")
num_usuario = abs(int(input("Ingrese un número entero: ")))

suma_total = 0

for numero in range(num_usuario + 1):
    suma_total += numero

print(f"La suma total es: {suma_total}")

# Ejercicio 8:
print("EJERCICIO 8: ")

numeros = []
pares = 0
impares = 0
positivos = 0
negativos = 0
rango = 10

for i in range(rango):
    numer = int(input(f"Ingresa el {i + 1}° número entero: "))
    numeros.append(numer)

for numer in numeros:
    if numer % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numer > 0:
        positivos += 1
    elif numer < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

# Ejercicio 9:
print("EJERCICIO 9: ")
numeros = []
suma_total = 0
rango = 10

for i in range(rango):
    numero = int(input(f"Ingresa el {i + 1}° número entero: "))
    numeros.append(numero)
    suma_total += numero

media = suma_total / rango

print(f"La media de los números ingresados es: {media}")

# Ejercicio 10:
print("EJERCICIO 10: ")

numero_derecho = int(input("Ingrese un número entero: "))
numero_string = str(numero_derecho)
numero_reves = numero_string[::-1]

print(f"El número invertido es: {numero_reves}")

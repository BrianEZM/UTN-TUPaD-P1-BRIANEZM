# 1.
var_lista_numero_rango4 = [num for num in range(4, 101, 4)]
print(var_lista_numero_rango4)

# 2.
mi_lista = ["rojo", "azul", "verde", "amarillo", "naranja"]
print(mi_lista[-2])

# 3.
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("python")
print(lista_vacia)

# 4.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5.
numeros_ejerc5 = [8, 15, 3, 22, 7]
numeros_ejerc5.remove(max(numeros_ejerc5))
print(numeros_ejerc5)
explicacion = "Este código primero declara e inicializa una lista con valores numéricos. Luego usa el método “remove()” para eliminar el elemento recibido por parametro. Este valor será el mas grande de la lista ya que se usa el método “max()” con la lista declarada. Por ultimo se imprime la lista con lo valores correspondientes, que serán los inicializados, pero sin el 22 (el valor máximo removido)."

# 6.
lista_numeros = list(range(10, 31, 5))
print(lista_numeros[:2])

# 7.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "corsa"
print(autos)

# 8.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# 9.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][compras[1].index("fideos")] = "tallarines"
compras[0].remove("pan")
print(compras)

# 10.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

# Crea una lista de números
numeros = [1, 2, 2, 3, 4, 4, 5]

# Convierte la lista a un set para eliminar duplicados
numeros_unicos = set(numeros)

# Crea un diccionario que cuente cuántas veces aparece cada número
conteo = {num: numeros.count(num) for num in numeros_unicos}

# Convierte el resultado a una lista de tuplas (número, conteo)
resultado = list(conteo.items())

print(f"Lista original: {numeros}")
print(f"Set de números únicos: {numeros_unicos}")
print(f"Diccionario de conteo: {conteo}")
print(f"Lista de tuplas (número, conteo): {resultado}")
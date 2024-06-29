'''
#List Comprehension simple
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

#Con condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Salida: [0, 2, 4, 6, 8]

#Con múltiples condiciones
numeros = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(numeros)  # Salida: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#Con else
numeros = [1, 2, 3, 4, 5]
resultado = ['par' if x % 2 == 0 else 'impar' for x in numeros]
print(resultado)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']

#Anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [num for fila in matriz for num in fila]
print(aplanada)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Con funciones
def es_primo(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

primos = [x for x in range(100) if es_primo(x)]
print(primos)  # Salida: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Creando diccionarios
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Creando sets
vocales = {letra for letra in 'supercalifragilisticoespialidoso' if letra in 'aeiou'}
print(vocales)  # Salida: {'a', 'e', 'i', 'o', 'u'}
'''
#ejercicio
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [(x, 'primo' if es_primo(x) else 'no primo') for x in range(1, 21)]
print(primos)
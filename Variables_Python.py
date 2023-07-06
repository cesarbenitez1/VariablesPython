#Definición de variables de tipo primitivo
entero = 7
flotante = 2.25
booleano = True
cadena = "Hello"

# 1. concatenar las variables en una cadena
resultado = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano)

# 2. límite de los enteros y los flotantes en python

# Límites en enteros:los enteros no tienen un límite específico. Son de precisión arbitraria, lo que significa que pueden representar enteros de tamaño ilimitado en teoría. 
# El único límite práctico es la memoria disponible en el sistema.
lim_entero = "No hay un límite específico para los enteros en Python, el único límite práctico es la memoria disponible en el sistema"

# Limites en flotantes:  Los flotantes se implementan utilizando el estándar IEEE 754 de punto flotante de doble precisión (64 bits)
# El límite máximo para flotantes positivos es aproximadamente 1.8e308 y el límite mínimo es aproximadamente -1.8e308
lim_flotante = "El límite máximo para flotantes positivos es aproximadamente 1.8e308 y el límite mínimo es aproximadamente -1.8e308."

# fórmula de la suma de los primeros n números pares
# La fórmula de la suma de los primeros n números pares es: n * (n + 1)
n = 4
suma_pares = n * (n + 1)

# Imprimir los resultados de los ejercicios anteriores
print("Concatenación:", resultado)
print("Limite de enteros:", lim_entero)
print("Limite de Flotantes:", lim_flotante)
print("La suma de los primeros", n , "numeros pares es:", suma_pares)
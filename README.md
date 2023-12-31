# Activ7
# Punto #1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado:

```
for numero in range(1, 101):
    cuadrado = numero ** 2
    print(f"Número: {numero}, Cuadrado: {cuadrado}")
```
#  Respectivo diagrama de flujo:
![mermaid-diagram-2023-10-11-223111](https://github.com/LauraDa999/Activ7/assets/141860731/c601ceb7-f5ed-4e20-bd08-ea373ce81dff)


#  Punto #2
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000:

```
Para numeros Impares:
print("Números impares desde 1 hasta 999:")
for numero_impar in range(1, 1000, 2):
    print(numero_impar)

Para numeros pares:
print("\nNúmeros pares desde 2 hasta 1000:")
for numero_par in range(2, 1001, 2):
    print(numero_par)
```
# Respectivo diagrama de flujo:

#  Punto #3
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado:
```
n = int(input("Ingrese un número natural n ≥ 2: "))

if n < 2:
    print("Por favor, ingrese un número natural mayor o igual a 2.")
else:
    for i in range(n, 1, -2):
        if i % 2 == 0:
            print(i)
```
#  Respectivo diagrama de flujo:





# Punto #4
 Desarrollar un algoritmo para informar en que año la población del país B superará a la de A:

```
# Población inicial de los países A y B
poblacion_A = 25  # En millones
poblacion_B = 18.9  # En millones

# Tasas de crecimiento anual de los países A y B (en decimal)
tasa_crecimiento_A = 0.02  # 2%
tasa_crecimiento_B = 0.03  # 3%

# Inicializamos un contador de años
anio = 2022

# Mientras la población de B sea menor o igual a la de A
while poblacion_B <= poblacion_A:
    # Calcula la población para el siguiente año
    poblacion_A = poblacion_A * (1 + tasa_crecimiento_A)
    poblacion_B = poblacion_B * (1 + tasa_crecimiento_B)
    anio += 1

# Imprime el año en el que la población de B supera a la de A
print(f"En el año {anio}, la población de B ({poblacion_B:.2f} millones) superará a la población de A ({poblacion_A:.2f} millones).")
```

# Punto #5
Imprimir el factorial de un número natural n dado:

```
n = int(input("Ingrese un número natural n: "))

if n < 0:
    print("El factorial no está definido para números negativos.")
elif n == 0:
    print("El factorial de 0 es 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}.")

```

# Punto #6

Enigma Numerico

Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual:
```
import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("Bienvenido a Enigma numerico.")

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        print(f" Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break
```

# Punto #7
Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores:

```
numero = int(input("Ingresa un número entre 2 y 50: "))

if 2 <= numero <= 50:
    print(f"Los divisores de {numero} son:")
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
else:
    print("El número ingresado no está dentro del rango especificado.")
```

#  Punto #8
Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones


```

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_hasta_100():
    primos = []
    for numero in range(1, 101):
        if es_primo(numero):
            primos.append(numero)
    return primos

primos = numeros_primos_hasta_100()
print("Números primos del 1 al 100:")
print(primos)
```

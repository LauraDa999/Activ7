# Activ7
# Punto #1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado:

```
for numero in range(1, 101):
    cuadrado = numero ** 2
    print(f"Número: {numero}, Cuadrado: {cuadrado}")
```
#Respectivo diagrama de flujo:
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


#  Punto 2
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

```mermaid
    Start[Inicio] --> Impares
    Start --> Pares
    Impares[Imprimir Números Impares] --> ForImpares[For numero_impar in range(1, 1000, 2):]
    ForImpares --> PrintImpar[Imprimir numero_impar]
    PrintImpar --> ForImparesCond[¿Siguiente número impar?]
    ForImparesCond --> ForImpares[Si]
    ForImparesCond --> EndImpares[No]
    EndImpares[Fin Impares] --> Stop[Detener]

    Pares[Imprimir Números Pares] --> ForPares[For numero_par in range(2, 1001, 2):]
    ForPares --> PrintPar[Imprimir numero_par]
    PrintPar --> ForParesCond[¿Siguiente número par?]
    ForParesCond --> ForPares[Si]
    ForParesCond --> EndPares[No]
    EndPares[Fin Pares] --> Stop
```
#  Punto 3

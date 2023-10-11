
numero = int(input("Ingresa un número entre 2 y 50: "))

if 2 <= numero <= 50:
    print(f"Los divisores de {numero} son:")
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
else:
    print("El número ingresado no está dentro del rango especificado.")


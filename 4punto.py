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
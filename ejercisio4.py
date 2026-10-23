# Leer los valores de min y max
min_valor = int(input("Introduce el valor mínimo: "))
max_valor = int(input("Introduce el valor máximo: "))

# Imprimir la tabla
print(f"{'Valor':<10} {'Cubo':<10}")

for valor in range(min_valor, max_valor + 1):
    cubo = valor ** 3
    print(f"{valor:<10} {cubo:<10}")

# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Validar que el número sea positivo
if n <= 0:
    print("El número debe ser positivo")
else:
    print(f"Números impares desde 1 hasta {n}:")

    # Iterar a través de todos los números desde 1 hasta n
    for num in range(1, n + 1):
        if num % 2 == 0:
            pass  # No hacer nada si el número es par
        else:
            print(num)
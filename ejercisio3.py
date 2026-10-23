# Solicitar al usuario un número entero mayor que 0
n = int(input("Introduce un número entero mayor que 0: "))

# Validar que el número sea mayor que 0
if n <= 0:
    print("El número debe ser mayor que 0")
else:
    print(f"Números primos menores que {n}:")

    # Iterar a través de todos los números menores que n
    for num in range(2, n):

        # Asumir que el número es primo
        es_primo = True

        # Comprobar si el número es primo
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        # Si es primo imprimir el numero
        if es_primo:
            print(num)

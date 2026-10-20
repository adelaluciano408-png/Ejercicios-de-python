def mostrar_menu():
    print("\n===== TRANSPORTE =====")
    print("1. Calcular tarifa")
    print("2. Consultar descuentos")
    print("3. Salir")


def calcular_tarifa():
    try:
        edad = int(input("Ingresa la edad del pasajero: "))
        distancia = int(input("Ingresa la distancia recorrida en km: "))

        if edad < 0 or distancia < 0:
            print("Error: la edad y la distancia deben ser valores positivos.")
            return

        tarifa_base = distancia * 3

        if edad < 12:
            porcentaje_desc = 0.50
        elif 12 <= edad <= 17:
            porcentaje_desc = 0.30
        elif 18 <= edad <= 59:
            porcentaje_desc = 0.00
        else:
            porcentaje_desc = 0.40

        descuento_aplicado = tarifa_base * porcentaje_desc
        total = tarifa_base - descuento_aplicado

        print("\n===== RESUMEN DEL BOLETO =====")
        print(f"Tarifa base: ${tarifa_base:.2f}")
        print(f"Descuento ({int(porcentaje_desc * 100)}%): -${descuento_aplicado:.2f}")
        print(f"Total a pagar: ${total:.2f}")

    except ValueError:
        print("Error: por favor ingrese valores numéricos válidos.")


def consultar_descuentos():
    print("\n===== TABLA DE DESCUENTOS =====")
    print("Menores de 12 años: 50% de descuento")
    print("De 12 a 17 años: 30% de descuento")
    print("De 18 a 59 años: tarifa normal")
    print("60 años o más: 40% de descuento")


def main():
    opcion = ""

    while opcion != "3":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            calcular_tarifa()
        elif opcion == "2":
            consultar_descuentos()
        elif opcion == "3":
            print("\nGracias por utilizar el sistema de transporte.")
        else:
            print("Opción no válida, por favor intente con 1, 2 o 3.")


if __name__ == "__main__":
    main()


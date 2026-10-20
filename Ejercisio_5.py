
def realizar_compra():
    print("\n--- REALIZAR COMPRA ---")

    nombre = input("Nombre del cliente: ")

    print("\nTipos de cliente:")
    print("1. Estudiante")
    print("2. Docente")
    print("3. Publico general")

    tipo = input("Selecciona el tipo de cliente: ")

    if tipo not in ["1", "2", "3"]:
        print("Tipo de cliente no valido.")
        return

    monto = float(input("Monto de la compra: $"))

    if monto < 0:
        print("El monto no puede ser negativo.")
        return

    if tipo == "1":
        cliente = "Estudiante"
        if monto >= 1000:
            descuento = 0.15
        else:
            descuento = 0.10

    elif tipo == "2":
        cliente = "Docente"
        if monto >= 1000:
            descuento = 0.20
        else:
            descuento = 0.15

    else:
        cliente = "Publico general"
        if monto >= 1000:
            descuento = 0.05
        else:
            descuento = 0.00

    monto_descuento = monto * descuento
    total = monto - monto_descuento

    print("\n===== RESUMEN DE COMPRA =====")
    print("Nombre del cliente:", nombre)
    print("Tipo de cliente:", cliente)
    print(f"Monto original: ${monto:.2f}")
    print(f"Porcentaje de descuento: {descuento * 100:.0f}%")
    print(f"Monto descontado: ${monto_descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")


def consultar_descuentos():
    print("\n===== TABLA DE DESCUENTOS =====")
    print("Estudiante:")
    print("  Compra >= $1000: 15%")
    print("  Compra < $1000: 10%")

    print("\nDocente:")
    print("  Compra >= $1000: 20%")
    print("  Compra < $1000: 15%")

    print("\nPublico general:")
    print("  Compra >= $1000: 5%")
    print("  Compra < $1000: 0%")


def menu():
    while True:
        print("\n===== TIENDA =====")
        print("1. Realizar compra")
        print("2. Consultar descuentos")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            realizar_compra()
        elif opcion == "2":
            consultar_descuentos()
        elif opcion == "3":
            print("Gracias por utilizar el sistema.")
            break
        else:
         print("Opcion no valida. Intenta nuevamente.")


menu()

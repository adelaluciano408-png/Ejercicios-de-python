
def pedir_numero(mensaje):
    """Pide un numero entre 0 y 100 y repite hasta que sea valido."""
    while True:
        try:
            valor = float(input(mensaje))

            if 0 <= valor <= 100:
                return valor

            print("Error: el valor debe estar entre 0 y 100.")

        except ValueError:
            print("Error: escribe un numero valido.")


def evaluar_aspirante():
    nombre = input("Nombre del aspirante: ")

    promedio = pedir_numero("Promedio escolar (0-100): ")
    examen = pedir_numero("Calificacion del examen de ingreso (0-100): ")

    if promedio >= 80 and examen >= 70:
        print(f"\n{nombre}: ACEPTADO. Felicidades, ingresaste.")

    elif promedio >= 80 and examen < 70:
        print(f"\n{nombre}: REQUIERE SEGUNDA EVALUACION.")

    else:
        print(f"\n{nombre}: NO ACEPTADO. Tu promedio es menor a 80.")


def consultar_criterios():
    print("\n--- CRITERIOS DE ADMISION ---")
    print("Promedio >= 80 y examen >= 70: Aceptado")
    print("Promedio >= 80 y examen < 70: Requiere segunda evaluacion")
    print("Promedio < 80: No aceptado")


def main():
    opcion = ""

    while opcion != "3":
        print("\n===== ADMISION =====")
        print("1. Evaluar aspirante")
        print("2. Consultar criterios")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            evaluar_aspirante()

        elif opcion == "2":
            consultar_criterios()

        elif opcion == "3":
            print("Saliendo del programa...")

        else:
            print("Opcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    main()






    
    
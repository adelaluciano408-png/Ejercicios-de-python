
print("===== MENU =====")
print("1 verificar el acceso")
print("2 Mostrar reglas")
print("3 salir")

opcion = input("seleccionar una opcion: ")

if opcion == "1":
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    credenciales = input("¿Tienes credenciales? (si/no): ").lower()

    if edad >= 20 and credenciales == "si":
        print("puedes ingresar")
    elif edad >= 20 and credenciales == "no":
        print("debe tramitar credencial")
    elif edad < 18 and credenciales == "si":
        print("puede ingresar acompañado")
    else:
        print("No puedes ingresar")

elif opcion == "2":
    print("Reglas de acceso:")
    print("Debes cumplir con los requisitos de edad y credenciales.")

elif opcion == "3":
    print("Saliendo del programa")

else:
    print("Opcion no valida")

print("===== MENU =====")
print ("1 verificar el acceso")
print ("2 Mostrar reglas")
print ("3 salir")

opcion = input ("seleccionar una opcion: ")
if opcion == "1":
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("ingresa tu edad: "))
    credenciales = input("¿Tienes credenciales? (si/no): "). lower()
    if edad >=20 and credencial == "si":
        print ("puedes ingresar")
    elif edad >= 20 and credenciales == "no":
        print ("debe tramitar credencial")
    elif edad < 18 and credencial == "si":
        print("puede ingresar acompañado")

    else:
        print ("no pude ingresar")

elif opcion == "2":
    print("\n===== REGLAS DE ACCESO =====")
    print("18 o más + credencial: Puede ingresar")
    print("18 o más + sin credencial: Debe tramitar credencial")
    print("Menor de 18 + credencial: Puede ingresar acompañado")
    print("Menor de 18 + sin credencial: No puede ingresar")



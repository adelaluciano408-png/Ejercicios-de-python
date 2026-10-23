# Solicitar al usuario dos años
anyo1 = int(input("Introduce el primer año: "))
anyo2 = int(input("Introduce el segundo año: "))

# Determinar el rango de años en orden decreciente
if anyo1 < anyo2:
    anyo1, anyo2 = anyo2, anyo1

# Iterar a través de los años en orden decreciente y mostrar los años bisiestos
print(f"Años bisiestos entre {anyo1} y {anyo2}:")

for anyo in range(anyo1, anyo2 - 1, -1):
    if (anyo % 4 == 0 and anyo % 100 != 0) or (anyo % 400 == 0):
        print(anyo)
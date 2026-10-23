#Solicitar al usuario que introduza una frase
frase = input("introduzca una frase: ")

#Solicitar al usuario que introdusza una letra
letra = input("Introduzca una letra: ")

#Contar el numero de ocurrencias de la letra en la frase
num_ocurrencias = 0
for char in frase:
    if char == letra:
        num_ocurrencias += 1

#Sustituir la letra por "*"
nueva_frase = ""
for char in frase:
    if char == letra:
        nueva_frase += "*"
    else:
        nueva_frase +=char

#Mostrar los resultados 
print(f"la letra'{letra}´ aparece {num_ocurrencias} veces en la frase.")
print(f"la nueva frase es: {nueva_frase}")

# Leer altura del triangulo
altura = int(input("introduce la altura del angulo invertido: "))

#Dibujar el triangulo invertido

for i in range(altura, 0, -1):
    espacios = altura -i
    estrellas = i
    print (' ' * espacios + '*' * estrellas)

#Dibujar el triangulo invertido de forma iterativa
for i in range(altura, 0, -1):
    #Imprimir los espacios
    for j in range(altura - i):
        print('', end='')
    #imprimir los asteriscos
    for k in range(i):
        print('*', end='')
    #Nueva linea despues de cada fila
    print()
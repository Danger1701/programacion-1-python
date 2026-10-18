# <= DESAFÍO 25 =>

# importo numpy bajo seudonimo np
import numpy as np # type: ignore
# importo random para crear los barcos
import random as r

r.randint(0, 4)

# Creo una matriz de zeros de 5 x 5
tab = np.zeros((5, 5))

# funcion que crea los barcos
def barcos():
    # uso una variable de conteo
    count = 0
    # mientras count sea menor q 3
    while count < 3:
        # creo dos valores entre 0 y 4 aleatorios
        x = r.randint(0, 4)
        y = r.randint(0, 4)
        if tab[x, y] == 0:
            tab[x, y] = 1
            count += 1

# ejecuto la funcion barcos()
barcos()

# mensaje de bienvenida la juego
print("<= BIENVENIDOS A: BATALLA NAVAL =>")

def atack():
    # uso una variable de conteo
    count = 0
    # mientras count sea menor q 3
    while count < 3:

        # pido ingresar coordenadas entre 1 y 5
        print(" \n<= INGRESE LAS COORDENADAS DE SIGUIENTE ATAQUE =>")
        # busque como hacer para que si un dato invalido es ingresado
        # no se crashee el programa
        while True:
            try:
                x = int(input("Ingrese una fila (1-5): ")) - 1
                y = int(input("Ingrese una columna (1-5): ")) - 1
                # si no es valido, el break vuelve al try
                break
            # y solicita volver a ingresar numeros enteros
            except ValueError:
                print("Debes ingresar números enteros")

        # si los enteros estan entre 0 y 4 no son validos
        if not (0 <= x <= 4 and 0 <= y <= 4):
            print("Coordenadas inválidas")
            # el continue vuelve al: while count < 3
            continue

        if tab[x, y] == 1:
            tab[x, y] = 8
            count += 1
            print("Exelente, el ataque ha derriba un barco")
        else:
            print("El ataque no alcanza ningun objetivo")

atack()

# Mensaje de juego termnado
print("<= HAS GANADO =>")
print("<= GAME OVER =>")
# printeo el mapa
for i in range (5):
    print(tab[i])

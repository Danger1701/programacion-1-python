# <= DESAFIO 4 =>

# creo una funcion para sumar los numeros pares de una lista
def desafio_4(lista):

    # creo una variable para ir sumando los numero pares
    result = 0

    # itero la lista
    for n in lista:
        # condición: que resto de la division sea 0 (es numero par)
        if n % 2 == 0:
            # sumo este par al valor de "result"
            result += n

    # retorno el valor de "result"
    return result


# creo la lista lista1 para testear
lista1 = [1, 2, 3, 4]
print("lista1 = ", desafio_4(lista1))
# resultado esperado = 6

# creo la lista lista2 para testear
lista2 = [4, 13, 35, 40]
print("lista2 = ", desafio_4(lista2))
# resultado esperado = 44

# creo la lista lista3 para testear
lista3 = [2, 3, 5, 8, 70, 100]
print("lista3 = ", desafio_4(lista3))
# resultado esperado = 180


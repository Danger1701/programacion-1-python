# <= DESAFIO 3 =>

# creo una funcion para sumar los primeros "n" numero naturales
def desafio_3(n):

    # creo una variable para ir sumando la "n" cantidad de numeros
    result = 0

    # itero con range() desde 0 hsata el numero "n+1" (xq 0 es el primer valor de range())
    for i in range(n+1):
        # sumo el valor de "i" a "result"
        result += i

    # retorno el valor de "result"
    return result


# ejecto desafio_3(4)
print("del o al 4 suman = ", desafio_3(4))
# resultado esperado = 10

# ejecto desafio_3(5)
print("del o al 5 suman = ", desafio_3(5))
# resultado esperado = 15

# ejecto desafio_3(10)
print("del o al 10 suman = ", desafio_3(10))
# resultado esperado = 55
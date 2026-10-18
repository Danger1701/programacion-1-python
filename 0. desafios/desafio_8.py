# <= DESAFIO 8 - Verificar múltiplos de varios números =>

# creo una funcion para verificar multiplos de un numero
def desafio_8(num):

    # creo una lista para de numeros a comprobar
    lista = [ 2, 3, 5, 7, 9, 10, 11 ]

    # creo una lista de resultados
    result = []

    # itero la lista
    for d in lista:
        # condición: que resto de la division sea 0 (es divisor)
        
        if num % d == 0:
            # agrego que SI es divisor a "result"
            result.append(f"{d} SI es divisor de {num}")
            
        else:
            # agrego que NO es divisor a "result"    
            result.append(f"{d} NO es divisor de {num}")

    # retorno la lista de resultados
    return result

# <= TESTS =>

# para el numero 3
print("<= para el numero 3 =>")
for i in desafio_8(3):
    print(i)

# para el numero 10
print("<= para el numero 10 =>")
for i in desafio_8(10):
    print(i)

# para el numero 33
print("<= para el numero 33 =>")
for i in desafio_8(33):
    print(i)

# <= DESAFÍO 32 =>

# importo math para poder usar isqrt()
import math

# creo una funcion para verificar si un número es primo
def es_primo(num):

    # filtro num si es 1 o menor, o si no es un entero
    if num < 2 or type(num) != int: return False

    # la ia que corrije me pidió que optimice la funcion
    # por ley, un numero que tenga un divisor, necesita otro para poder contruirse
    # ej: 100 = 50 x 2
    # pero uno de esos divisores tiene que ser menor q la raiz cuadrada del numero
    # ej: 10x10=100... por ejemplo... no puede 20x15 nunca dar 100...
    # xq ambos son mayores que la raiz cuadrada de 100
    # utilizo el metodo isqrt(), que devuelve el entero de la raíz cuadrada entera de un número
    # para iterar, y le sumo 1 para q incluya a la raiz cuadrada tambien
    # itero entre un rango (2, math.isqrt(num)+1)
    for n in range (2, math.isqrt(num)+1):
        if num % n == 0 : return False
    
    # sí no
    return True

# creo una funcion para contar los primos de una lista
def cant_primos(nums):

    #creo una variable para devolver
    # result = 0

    # creo result para mostrar los mismos
    result = 0

    # itero la lista nums
    for n in nums:
        # evaluó cada n según la función es_primo()
        if es_primo(n):
            result += 1

    # devuelvo la cantidad de números primos
    return result

# creo una función main() que cree la lista y llame las otras funciones
def main():

    # resultado esperado 9
    lista = [-1, 1, 2, 3, 5, 6, 7, 8, 9, 10, 10.3, 11.0, 13, 29, 142, 8999, 12853, 29989]

    print(cant_primos(lista))

# llamo a main()
main()

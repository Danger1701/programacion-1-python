# <= DESAFIO 7 - Convertidor de temperaturas =>

# creo una funcion que recibe una temperaturas (Celcius)
def desafio_7(c):

    # creo dos variables para los resultados (Fahrenheit y Kelvin)
    
    f = c * 9/5 + 32

    k = c + 273.15

    # retorno los valores resultantes
    return f, k

# <= TESTS =>

# para 0 Celcius
print(desafio_7(0)[0], " Fahrenheit // esperado: 32.0")
print(desafio_7(0)[1], " Kelvin // esperado: 273.15")

# para 20 grados Celcius
print(desafio_7(20)[0], " Fahrenheit // esperado: 68.0 Fahrenheit")
print(desafio_7(20)[1], " Kelvin // esperado: 293,15 Kelvin")

# para 33 grados Celcius
print(desafio_7(33)[0], " Fahrenheit// esperado: 91,4")
print(desafio_7(33)[1], " Kelvin// esperado: 306,15")

# Desafío 70: excepción personalizada llamada NegativeNumberError

# creo la excepción propia con class
class NegativeNumberError(Exception):
    pass

# uso el try para hacer una ejecucion controlada
try:
    num = int(input("Ingrese un número: "))

    # si el numero es negativo
    if num < 0:
        # raise lanza manualmente un error, para ser capturado con el except
        raise NegativeNumberError("No se puede calcular la raiz cuadrada de un numero negativo")

    resultado = num**(1/2)

# recupera NegativeNumberError
# el as "error", es obligatorio, aunque la variable puede llamarse
except NegativeNumberError as error:
    print(error)

# sino hay errores...
else:
    # simplifico el resultado, sino solo permito 2 digitos
    print(f"resultado: {resultado:.2f}".rstrip("0").rstrip("."))

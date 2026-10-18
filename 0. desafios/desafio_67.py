# Desafío 67: try-except

# uso el try para que si algo falla, poder trabajar incluso con ese dato (la fasha)
try:
    # ingreso los valores
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    # los divido, entendiendo que puede fallar
    resultado = num1 / num2

# si es un problema de tipo de dato ingresado
except ValueError:
    print("Error: debe ingresar valores numéricos.")

# si es un problema de division de un numero entre 0
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

# sino hay errores...
# esta figura es opcional, pero me gusto lo que representa en lo didactico,
# ayudando a entender la figura completa del try
else:
    print("Resultado:", resultado)
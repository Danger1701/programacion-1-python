# Desafío 65: Figuras - Area()

# Creo la clase Figura
class Figura:

    # creo area para calcular el area de la figura
    def area(self):
        # pero uso pass para no hacer nada, segun entendí,
        # xq el calculo se da en la sub clase
        pass

# Creo Círculo, como subclase de Figura
class Circulo(Figura):
    # Creo el atriburo radio para calcular el area
    def __init__(self, radio):
        self.__radio = radio
    # Creo area para sobreescribir la funcion de Figura
    def area(self):
        return f"El área del círculo con radio {self.__radio}, es {3.14 * self.__radio ** 2}"

# Creo Cuadrado, como subclase de Figura
class Cuadrado(Figura):
    # Creo el atriburo lado para calcular el area
    def __init__(self, lado):
        self.__lado = lado
    # Creo area para sobreescribir la funcion de Figura
    def area(self):
        return f"El área del cuadrado con lado: {self.__lado},  es {self.__lado ** 2}"

# creo un Circulo
circulo1 = Circulo(
    radio=1
)

# creo un Cuadrado
cuadrado1 = Cuadrado(
    lado=2
)

# muestro los datos
print(circulo1.area())
print(cuadrado1.area())
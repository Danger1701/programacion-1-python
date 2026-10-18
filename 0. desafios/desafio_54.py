# Desafío 54
# Crea los atributos nombre y nacionalidad, como privados 

class Autor:
    # utilizo "__" para determinar los atributos como privados 
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    # defino las funciones para poder acceder a los datos privados
    @property
    def nombre(self):
        return self.__nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # defino las funciones para poder modificar los valores
    # no permitiendo q un string vacio sea setteado
    @nombre.setter
    def nombre(self, new_nombre):
        if new_nombre != "":
            self.__nombre = new_nombre
        else:
            print("No se pudo modificar el dato")

    @nacionalidad.setter
    def nacionalidad(self, new_nacionalidad):
        if new_nacionalidad != "":
            self.__nacionalidad = new_nacionalidad
        else:
            print("No se pudo modificar el dato")

# creo un autor
autor1 = Autor(
    nombre="Gabriel García Márquez",
    nacionalidad="Colombiana"
)

# muestro los datos
print(autor1.nombre)
print(autor1.nacionalidad)

# intento modificar un dato con un string vacio
autor1.nacionalidad = ""

# modifico el dato de nacionalidad a "colombiano"
autor1.nacionalidad = "Colombiano"

# muestro los datos actualizados
print(autor1.nombre)
print(autor1.nacionalidad)
# Desafío 57: Herencia — clase poeta

# Defino la clase Autor# Crea los atributos nombre y nacionalidad, como privados 
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def nacionalidad(self):
        return self.__nacionalidad

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

class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # utilizo super().__init__ para heredar los atributos de autor
        super().__init__(nombre, nacionalidad)
        # añado el atributo 
        self.__tipo_poesia = tipo_poesia

    # creo datos para devolver la informacion de cada poeta
    @property
    def datos(self):
        return self.nombre, self.nacionalidad, self.__tipo_poesia

# creo un poeta1
poeta1 = Poeta(
    nombre="Pablo Neruda",
    nacionalidad="Chileno",
    tipo_poesia= "Romántica"
)

# creo un poeta2
poeta2 = Poeta(
    nombre="Federico García Lorca",
    nacionalidad="Español",
    tipo_poesia= "Lírica"
)

# muestro los poetas
print(poeta1.datos)
print(poeta2.datos)
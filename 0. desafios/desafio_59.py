# Desafío 59: LibroDigital - Herencia de clase Libro

# copio libro del desafio_48
class Libro:
    def __init__(self, titulo="", genero="", ISBN=""):
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN

class LibroDigital(Libro):
    def __init__(self, titulo, genero, ISBN, formato, tamaño_archivo):
        # utilizo super().__init__ para heredar los atributos de libro
        super().__init__(titulo, genero, ISBN)
        # añado atributos
        self.__formato = formato
        self.__tamaño_archivo = tamaño_archivo

    # creo datos para devolver la informacion de cada libre digital
    @property
    def mostrar_informacion(self):
        return self.titulo, self.genero, self.ISBN, self.__formato, self.__tamaño_archivo

class EBook(LibroDigital):
    def __init__(self, titulo, genero, ISBN, formato, tamaño_archivo, enlace_descarga):
        # utilizo super().__init__ para heredar los atributos del libro digital
        super().__init__(titulo, genero, ISBN, formato, tamaño_archivo)
        # añado el atributo 
        self.__enlace_descarga = enlace_descarga

    # creo datos para devolver la informacion de cada ebook
    @property
    def mostrar_informacion(self):
        # averigue que se podian heredar funciones tambien
        # puedo aplicarselo a la herencia anterior pero
        # creo que es mas grafico asi...
        return super().mostrar_informacion + (self.__enlace_descarga,)

# creo un LibroDigital
digital1 = LibroDigital(
    titulo="A La Escucha",
    genero="Filosofía",
    ISBN= "9788461090150",
    formato="pdf",
    tamaño_archivo="10.4 MB"
)

# creo un EBook
ebook1 = EBook(
    titulo="A La Escucha",
    genero="Filosofía",
    ISBN= "9788461090150",
    formato="pdf",
    tamaño_archivo="10.4 MB",
    enlace_descarga="https://drive.google.com/drive/u/1/folders/12QbrQKPyCD0sJLB1H7_7LQHHPi7Fm1he"
)

# muestro los datos
print(digital1.mostrar_informacion)
print(ebook1.mostrar_informacion)
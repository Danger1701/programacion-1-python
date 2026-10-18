# Desafío 48
# Crea una clase Libro con atributos como título, género e ISBN. 

# similar a autor... creo la class Libro, con sus respectivas necesidades
class Libro:
    def __init__(self, titulo="", genero="", ISBN=""):
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN

    # creo la funtion para poder mostrar un libro
    def mostrar_libros(self):
        print(f"titulo: {self.titulo}")
        print(f"genero: {self.genero}")
        print(f"ISBN: {self.ISBN}")

# creo un libro
libro1 = Libro(
    titulo="Cien años de soledad",
    genero="Novela",
    ISBN="9788420471839"
)

# muestro un libro
# Libro.mostrar_libros(libro1)

# ¿Cómo podrías relacionar esta clase con la clase Autor?
# pordia importa la class Autor del otro archivo, pero como tiene
# varios prints, prefiero copiar la clas entera y listo

class Autor:
    # amplio la clase, agregando el atributo libros, q por defecto es None (nada)
    def __init__(self, nombre="", nacionalidad="", libros=None):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        # si libros es None pasa a ser un string vacio, 
        # sino es lo inicializado al crear el nuevo autor
        if libros is None:
            self.libros = []
        else:
            self.libros = libros

    # Método para mostrar los detalles del autor
    def mostrar_autor(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        # recorro el array libros
        for libro in self.libros:
            # muestro cada libro con la funcion mostrar_libros()
            libro.mostrar_libros()

    # Método para agregar libros al autor
    def agregar_libro(self, libro):
        self.libros.append(libro)

    # Método para eliminar libros al autor
    def eliminar_libro(self, libro):
        self.libros.remove(libro)

# creo un autor
autor1 = Autor(
    nombre="Gabriel García Márquez",
    nacionalidad="Colombiana",
    libros=[]
)

# creo otro libro
libro2 = Libro(
    titulo="El amor en los tiempos del cólera",
    genero="Novela",
    ISBN="9789871138135"
)

# agrego ambos libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# mas arriba... para poder mostrar los libros... edito la function mostrar_libros()

# muestro el autor
autor1.mostrar_autor()




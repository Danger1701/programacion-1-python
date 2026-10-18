# Desafío 47
# Amplía la clase Autor para incluir una lista de libros escritos por el autor. Implementa métodos para agregar y eliminar libros de esta lista.

# recupero del repartido la clase Autor
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
        print(f"Libros: {self.libros}")

# Método para agregar libros al autor
    def agregar_libro(self, libro):
        self.libros.append(libro)

# Método para eliminar libros al autor
    def eliminar_libro(self, libro):
        self.libros.remove(libro)

autor1 = Autor(
    nombre="Gabriel García Márquez",
    nacionalidad="Colombiana",
    libros=["Cien años de soledad"]
)

# muestro autor1 antes de agregar libro
autor1.mostrar_autor()

# agrego un libro
autor1.agregar_libro("El amor en los tiempos del cólera")

# muestro autor1 despues de agregar libro
autor1.mostrar_autor()

# elimino un libro
autor1.eliminar_libro("El amor en los tiempos del cólera")

# muestro autor1 despues de eliminar libro
autor1.mostrar_autor()
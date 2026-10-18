# creo una lista de libros

libros = [
    "Don Quijote de la Mancha",
    "El Principito", 
    "El Señor de los Anillos", 
    "Cien años de soledad",
    ]

# function para agegar un libro
def agregar(libro):
    return libros.append(libro)

# funcion para buscar un libro en la lista
def buscar(libro):
    return libro in libros

# function para eliminar un libro, si existe
def eliminar(libro):
    if libro in libros:
        libros.remove(libro)

# function que muestra todos los libros
def mostrar():
    return print(libros)

# muestro la lista inicial
print("Lista inicial:")
mostrar()

# agrego un libro
agregar("Harry Potter")

# busco un libro que existe y muestro el resultado
print("Existe Harry Potter ?")
print(buscar("Harry Potter"))

# busco un libro que no existe y muestro el resultado
print("Existe Animales Fantásticos ?")
print(buscar("Animales Fantásticos"))

# elimino "Cien años de soledad" de la lista
eliminar("Cien años de soledad")

# elimino un libro q no existe de la lista
eliminar("El Capital")

# muestro la lista final
print("Lista final:")
mostrar()
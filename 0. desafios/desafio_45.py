# creo una lista de libros en español

biblioteca = [
    "Orgullo y prejuicio",
    "El Principito", 
    "El Señor de los Anillos", 
    "Cien años de soledad",
    ]

# creo otra lista de libros en inglés 
library = [
    "Pride and Prejudice",
    "The Little Prince", 
    "The Lord of the Rings", 
    "One Hundred Years of Solitude",
    ]

# function para agegar un elemento a una lista
# primer arg: libro a ingresar, segundo biblioteca
def agregar(elemento, lista):
    return lista.append(elemento)

# funcion para buscar un elemento en una lista
# primer arg: libro a ingresar, segundo biblioteca
def buscar(elemento, lista):
    return elemento in lista

# function para eliminar elemento de lista, si existe
# primer arg: libro a ingresar, segundo biblioteca
def eliminar(elemento, lista):
    if elemento in lista:
        return lista.remove(elemento)

# function que muestra todos los elementos de una lista
# unico argumnento: biblioteca
def mostrar(lista):
    return print(lista)

# muestro la lista inicial
print("Lista inicial de Biblioteca")
mostrar(biblioteca)

# agrego un libro
agregar("Harry Potter", biblioteca)

# busco un libro que existe y muestro el resultado
print("Existe Harry Potter en biblioteca?")
print(buscar("Harry Potter", biblioteca))

# busco un libro que no existe y muestro el resultado
print("Existe Animales Fantásticos en biblioteca?")
print(buscar("Animales Fantásticos", biblioteca))

# elimino "Cien años de soledad" de biblioteca
print("Intento eliminar Cien años de soledad de biblioteca!")
eliminar("Cien años de soledad", biblioteca)

# elimino un libro q no existe de biblioteca
print("Intento eliminar El Capital de biblioteca!")
eliminar("El Capital", biblioteca)

# muestro la lista final
print("Lista final de biblioteca")
mostrar(biblioteca)

# ------

# muestro la lista inicial
print("Lista inicial de library")
mostrar(library)

# agrego un libro
agregar("Harry Potter", library)

# busco un libro que existe y muestro el resultado
print("Existe Harry Potter en library?")
print(buscar("Harry Potter", library))

# busco un libro que no existe y muestro el resultado
print("Existe Fantastic Beast en library?")
print(buscar("Fantastic Beast", library))

# elimino "Cien años de soledad" de library
print("Intento eliminar One Hundred Years of Solitude de library!")
eliminar("One Hundred Years of Solitude", library)

# elimino un libro q no existe de library
print("Intento eliminar Capital de library!")
eliminar("Capital", library)

# muestro la lista final
print("Lista final de library")
mostrar(library)
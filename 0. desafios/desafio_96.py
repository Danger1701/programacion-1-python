# Desafío 96: Inventario de productos con diccionarios

#Desarrolla un sistema de inventario para una tienda utilizando diccionarios, donde:
# *La clave es el código del producto.
# *El valor es otro diccionario con detalles como nombre, precio y cantidad en stock.

# El programa debe permitir:
# *Agregar nuevos productos
# *Actualizar el stock.
# *Buscar productos por código y mostrar sus detalles.

# Creo el inventario como un diccionario
inventario = {
    "0000": {
        "nombre": "Teclado",
        "precio": 1500,
        "stock": 10
    },
    "0001": {
        "nombre": "Mouse",
        "precio": 800,
        "stock": 20
    }
}

# Funtion para agregar un nuevo producto
def agregar_producto():
    # input de variable para el codigo
    codigo = input("Código del producto a agregar: ")
    # si ya existe un producto con ese codigo se cancela
    if codigo in inventario:
        print("El producto ya existe.")
        return
    # input de los datos del procuto
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock inicial: "))
    # uso los datos para agregar los datos formateados al inventario
    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    # muestro el producto
    print("Producto agregado correctamente.")

# Funtion para buscar y mostrar un producto
def buscar_producto():
    # input para ingresar el codigo a buscar
    codigo = input("Código del producto a buscar: ")

    # compara lo ingresado con las claves diccionario
    if codigo in inventario:
        # si existe coincidencia
        print(inventario[codigo])
    else:
        # si no responde esto
        print("Producto no encontrado.")

# Funtion para actualizar un producto
def actualizar_producto():
    # input para ingresar el codigo a actualziar
    codigo = input("Código del producto a actualizar: ")

    # compara lo ingresado con las claves diccionario
    if codigo in inventario:
        # si hay coincidencia
        # pide valores numericos para modificar el stock actual
        cantidad = int(input("Cantidad que desea agregar: "))
        # realiza la suma (o resta si el valor inresado es <0)
        inventario[codigo]["stock"] += cantidad

        print("Stock actualizado correctamente.")
    else:
        # si no hay coincidencia
        print("Producto no encontrado.")





agregar_producto()
actualizar_producto()
buscar_producto()
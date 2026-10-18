# Desafío 73: Lista de números repetidos

# Creo una lista de numero con algunos repetidos
lista_rep = [0, 1, 3, 5, 7, 3, 9, 0, 5, 3, 2, 2, 1, 3, 4, 5, 6, 7, 8, 7, 0]

# Creo una lista vacia q muestre los resultados
result = []

# hago un for para recorrer la lista
for n in lista_rep:
    # si el numero no pertenece a result, lo añado
    if n not in result:
        result.append(n)

# muestro la lista original
print("Lista original: ", lista_rep)
# muestro la lista sin repeticiones
print("Lista sin duplicados: ", result)
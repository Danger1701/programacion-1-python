# creo una function para invertir texto
def invert_text(text):

    # uso split() convertir a text en un array con palabras como elementos
    text = text.split()

    # creo una nueva lista vacia para re ordenar los elementos
    newtext = []

    # creo una funcion para hacer una inversion recursiva
    def recursive_invert_text(text):
        # cuando text este vacio retorna newtext
        if len(text) == 0:
            return newtext
          
        # inserto cada palabra al principio del nuevo array,
        # para dejar el orden invertido; la ultima primero.
        newtext.insert(0, text[0])
        # elimino el primer elemento de text
        text.pop(0)

        # llamo nuevamente la funcion
        return recursive_invert_text(text)
        
    # llamo la function recursive_invert_text()
    recursive_invert_text(text)

    # vuelvo a unir y retorno newtext con (" ") espacios entre palabras
    return " ".join(newtext)

print(invert_text("la vela puerca es la mejor banda del uruguay"))
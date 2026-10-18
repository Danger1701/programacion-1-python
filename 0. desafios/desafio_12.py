# <= DESAFÍO 12 =>

# importo string para poder usarlo
import string as string
    
# creo "texto" y guardo el texto ingresado
texto = input("Ingrese las palabras a contar:")

# valido que el texto no este vacio
if texto == "":
    # en caso de estar vacío, devuelvo el siguiente mensaje
    print("Usted no ingresó ninguna palabra. Gracias")
else:
    # utilizo string.punctuation para detectar los signos de puntuación
    for signo in string.punctuation:
        # reemplazo los signos de puntuación por un carácter vacío
        texto = texto.replace(signo, "")

    # separo el texto en palabras con split()
    result = texto.split()

    # retorno el valor del conteo de palabras
    print(f"El texto que ingresó tiene {len(result)} palabras.")
    print("Conteo completado correctamente")

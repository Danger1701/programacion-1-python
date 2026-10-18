# import el archivo y lo nombro como ANSI_style
import desafio_36_ANSI_styles as ANSI_styles

# creo una variable para comparar los prints
text = "Hola mundo!"

# imprimo en consola text en distintos formatos
print(text)
print(ANSI_styles.negrita(text))
print(ANSI_styles.cursiva(text))
print(ANSI_styles.subrayado(text))
print(ANSI_styles.tachado(text))
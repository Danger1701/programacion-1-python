# funcion para agregar estilo ANSI negrita
def negrita(text):
    return f"\033[1m{text}\033[0m"

# funcion para agregar estilo ANSI cursiva
def cursiva(text):
    return f"\033[3m{text}\033[0m"

# funcion para agregar estilo ANSI subrayado
def subrayado(text):
    return f"\033[4m{text}\033[0m"

# funcion para agregar estilo ANSI tachado
def tachado(text):
    return f"\033[9m{text}\033[0m"
# importo el modulo datetime
import datetime

# creo una function para solicitar fechas
def pedir_fecha():
    # solicito cada valor y lo guardo como texto... luego,
    # si el valor ingresado está vacio, adjudico el valor actual al mismo
    año = input("Ingrese año: ")
    año = datetime.datetime.now().year if año == "" else int(año)

    mes = input("Ingrese mes: ")
    mes = datetime.datetime.now().month if mes == "" else int(mes)

    dia = input("Ingrese día: ")
    dia = datetime.datetime.now().day if dia == "" else int(dia)

    hora = input("Ingrese hora: ")
    hora = datetime.datetime.now().hour if hora == "" else int(hora)

    minuto = input("Ingrese minuto: ")
    minuto = datetime.datetime.now().minute if minuto == "" else int(minuto)

    # creo el datetime con los valores ingreados
    fecha = datetime.datetime(
        year=año,
        month=mes,
        day=dia,
        hour=hora,
        minute=minuto
    )
    # devuelvo fecha
    return fecha

# solicito los valres de la primer fecha
print("<= Por favor ingrese los valores de la primer fecha =>")
fecha1 = pedir_fecha()
print("<= Por favor ingrese los valores de la segunda fecha =>")
fecha2 = pedir_fecha()

# evaluo la diferencia entre las fechas
# agrego abs para no recibir numero negativos
print("<= La diferencia entre las fechas es: =>")
print(abs(fecha1 - fecha2))
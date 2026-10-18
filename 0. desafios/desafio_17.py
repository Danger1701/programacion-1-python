# <= DESAFÍO 17 =>

# importo random para poder usarlo
import random as random

# creo un diccionario "cars", con el valor incial 0
cars = { "bmw": 0, "ford": 0, "fiat": 0, "volvo": 0, "audi": 0, "mazda": 0 }

# itero 10 veces
for i in range(10):
    # un auto de carrera avanza entre 60 y 105 m/s
    # cada random.randint simula los m/s de recorridos
    # y lo sumo al valor de cada objeto/valor de cars
    cars["bmw"] += random.randint(50, 100)
    cars["ford"] += random.randint(50, 100)
    cars["fiat"] += random.randint(50, 100)
    cars["volvo"] += random.randint(50, 100)
    cars["audi"] += random.randint(50, 100)
    cars["mazda"] += random.randint(50, 100)

# recupero el valor mas alto del diccionario
result = max(cars.values())

# para cada car de cars
for car in cars:
    # si su valor es igual a result
    if cars[car] == result:
        # imprimo ese car, pueden ser varios
        print(car, cars[car], "metros recorridos")
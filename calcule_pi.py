import random
import math
from statistic import standard_deviation, media 

def throw_needles(number_needles):
    inside_circle = 0 #cuantas cayeron adentro del circulo

    for _ in range(number_needles): #lanzar tanta halla number_needles
        x = random.random() * random.choice([-1, 1]) #para convertir random a entre -1 al 1
        y = random.random() * random.choice([-1, 1])
        distance_from_center = math.sqrt(x**2 + y**2) #raiz cuadrada /teorema pitagoras

        if distance_from_center <= 1:
            inside_circle += 1
    return (4 * inside_circle) / number_needles

#obtener medida de tendencia central
def estimate(number_needles, number_attempts): #generar estimacion / cuantas veces va a correr
    expected = [] #todas las estimaciones de Pi
    for _ in range (number_attempts):
        estimate_pi = throw_needles(number_needles)
        expected.append(estimate_pi) #estimamos muchas veces

    media_expected = media(expected)
    sigma = standard_deviation(expected)
    print(f'Expected={round(media_expected, 5)}, sigma={round(sigma, 5)}, needles={number_needles}')    
    return (media_expected, sigma)

#uso de la regla empirica
def estimated_pi(precision, number_attempts):
    number_needles = 1000
    sigma = precision

    while sigma >= precision / 1.96: #confiabilidad al 95%
        media, sigma = estimate(number_needles, number_attempts)
        number_needles *= 2  #en cada iteracion, multiplicar el numero de agujas
    return media

if __name__ == "__main__":
    estimated_pi(0.01, 1000)

#la desviacion estandar es menor en cada iteracion
#acercanos cada vez mas a una conclusion estadisticamente valida
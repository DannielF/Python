
from drunk import traditional_drunk
from field import Field
from coordinate import Coordinate
from bokeh.plotting import figure, show

def walk(field, drunk, steps):
    start = field.get_coordinate(drunk) #cual es el inicio

    for _ in range(steps): #realizar tanto pasos se nos digan
        field.move_drunk(drunk)

    return start.distance(field.get_coordinate(drunk)) #regresamos la distancia que recorrio y preguntar cual es la otra coord   

def simulate_walk(steps, times_attempts, traditional_drunk):
    drunk = traditional_drunk(name='Daniel') #inicializar variable/recibiendolo como parametro/agnostica
    origin = Coordinate(0, 0)
    distances = [] #variables/guardar distancias

    for _ in range(times_attempts): # _ <no se utiliza la variable/solo se da un rango
        field = Field() #la simulacion
        field.add_drunk(drunk, origin) #campo añadir borracho
        simulate_walk = walk(field, drunk, steps) #funcion auxiliar
        distances.append(round(simulate_walk, 1)) #añadir a las distancias, la simulacion
    return distances

def graphic(x, y):
    graphics= figure(title='Random path', x_axis_label='steps', y_axis_label='distance')
    graphics.line(x, y, legend_label='mid distance')

    show(graphics)    

def main(distance_walk, times_attempts, traditional_drunk):
    mid_distance_per_walk = []

    for steps in distance_walk:
        distances = simulate_walk(steps, times_attempts, traditional_drunk) #simular caminata/regresa arreglo de distancias
        distance_media = round(sum(distances) / len (distances), 4) #suma de las distancias dividido en las distancias recorridas
        distance_max = max(distances)
        distance_min = min(distances)
        mid_distance_per_walk.append(distance_media)
        print(f'{traditional_drunk.__name__} random walking of {steps} steps') #nombre de la clse borracho
        print(f'Media = {distance_media}')
        print(f'Max = {distance_max}')
        print(f'Min = {distance_min}')
    graphic(distance_walk, mid_distance_per_walk)

if __name__ == "__main__": #entry point /eso es lo que va a correr
    distance_walk = [10, 100, 1000, 10000,]
    times_attempts = 100

    main(distance_walk, times_attempts, traditional_drunk) #la misma clase como refencia

    #la simulacion se corre varias veces
    #para entender cual es la media de todas las simulaciones
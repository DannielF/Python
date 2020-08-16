#abstraccion de donde se encuentra el borracho en el plano 
class Coordinate:

    def __init__(self, x, y): #self>referencia a la propia instancia
        self.x = x #inicializar la variable
        self.y = y

    def move(self, delta_x, delta_y): #cuanto hacia la x y cuanto hacia la y
        return Coordinate(self.x + delta_x, self.y + delta_y) #regresar con los cambios en x 'y y   

    def distance(self, other_coord): #hasta donde es la distancia /metodo pitagoras
        delta_x = self.x - other_coord.x
        delta_y = self.y - other_coord.y
        return (delta_x**2 + delta_y**2)**0.5 # or math.sqrt

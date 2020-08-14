
class field:

    def __init__(self): #ningun parametro
        self.coordinate_drunks = {} #definir diccionario, recibir coordenadas

    def add_drunk(self, drunk, coordinate): #donde va borracho
        self.coordinate_drunks[drunk] = coordinate

    def move_drunk(self, drunk): # que borracho mover
        delta_x, delta_y = drunk.walk() #esto es aleatorio
        coordinate_currently = self.coordinate_drunks[drunk] #obtener coord del diccionario
        new_coord = coordinate_currently.move(delta_x, delta_y) #a donde se debe mover

        self.coordinate_drunks[drunk] #lo movimos adentro de nuestro campo

    def get_coordinate(self, drunk): #obtener coordenada/donde anda el borracho/calcular distancia
        return self.coordinate_drunks[drunk]    


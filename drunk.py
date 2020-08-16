import random


class drunk: #clase que represente a los borrachos

    def __init__(self, name): #definir constructor
        self.name = name

class traditional_drunk(drunk): # extiende a borracho

    def __init__(self, name):
        super().__init__(name) #obtener refrencia a la superclase con 'super'         

    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]) #generar opciones aleatoria   
                              #arriba y #abajo y   #derecha x #izquierda x
                              #cuando camina borracho regresa una tupla

#generar simulacion, para ver si la hipotesis de que cuanto mas 
#pasos da un borracho mas se aleja del origen, es cierta o falsa
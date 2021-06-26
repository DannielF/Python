
class Auto:

    def __init__(self, model, brand, color, year):
        self.model = model
        self.brand = brand
        self.color = color
        self.year = year
        self._status = 'waiting'
        self._motor = None

    def accelerate(self, type='slowly')
        if type == 'fast':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)

        self._status = 'moving'    

class Motor:

    def __init__(self, cylinders, hp, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self.hp = hp
        self._temperature = 0

    def inject_gasoline(self, quantity):

if __name__ == "__main__":
    __init__()
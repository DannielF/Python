
class laundry:

    def __init__(self):
        pass

    def wash(self, temperature='warm'):
        self._fill_tank_water(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()
        self._dry()

    def _fill_tank_water(self, temperature):
        print(f'Filling the tank with {temperature} water')

    def _add_soap(self):
        print('Add soap')        

    def _wash(self):
        print('Washing clothes')

    def _centrifuge(self):
        print('Centrifuge clothes')

    def _dry(self):
        print('Drying clothes')    

if __name__ == "__main__":
    laundry = laundry()
    laundry.wash()                
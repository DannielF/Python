
class Rectangule:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

class Square(Rectangule):

    def __init__(self, side):
        super().__init__(side, side)

if __name__ == "__main__":
    rectangule = Rectangule(base=3, height=4)
    print(rectangule.area())

    Square = Square(side=5)
    print(Square.area())                    


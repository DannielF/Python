
class coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coordinate):
        x_diff = (self.x - other_coordinate.x)**2
        y_diff = (self.y - other_coordinate.y)**2

        return (x_diff + y_diff)**0.5
        
if __name__ == "__main__":
    Coord_1 = coordinate(3, 30)
    Coord_2 = coordinate(4, 8)

    # print(Coord_1.distance(Coord_2))
    print(isinstance(Coord_2, coordinate))
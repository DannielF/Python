
class People:

    def __init__(self, name):
        self.name = name

    def forward(self):
        print('walking')    

class Cyclist(People):

    def __init__(self, name):
        super().__init__(name)

    def forward(self):
        print('ride a bike')            

def main():
    people = People('Daniel')
    people.forward()

    cyclist = Cyclist('David')
    cyclist.forward()

if __name__ == "__main__":
    main()
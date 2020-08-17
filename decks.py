import random
import collections

STICKS = ['swors', 'heart', 'diamond', 'clover']
VALUES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jei', 'queen', 'king']

def make_deck():
    decks = [] #array lista todas las barajas
    for stick in STICKS:
        for value  in VALUES:
            decks.append((stick, value)) #generar tupla
    return decks        

def get_deal(decks, size_hand): 
    hand = random.sample(decks, size_hand)
    return hand

def main(size_hand, attempts):
    decks = make_deck() #obtener nuestras barajas

    hands = [] #guardar todas la manos de la simulacion
    for _ in range(attempts): #correr los intentos solicitados
        hand = get_deal(decks, size_hand)
        hands.append(hand) 

    pairs = 0
    for hand in hands:
        values = [] #guardar los valores, cuantas veces hay un par
        for card in hand:
            values.append(card[1]) #obtener indice 1

        counter = dict(collections.Counter(values))
        for val in counter.values(): #ahora es un diccionario y se puede acceder directamente
            if val == 2: #solo par
                pairs += 1
                break #se el encontro el par y detenerse
    
    probability_pair = pairs / attempts #calcular probabilidad
    print(f'probability to find pair in a hand of {size_hand} decks is {probability_pair}')        

if __name__ == "__main__":
    size_hand = int(input('How many decks will the hand be: '))
    attempts = int(input('How many attempts to calculate the probability: '))

    main(size_hand, attempts)
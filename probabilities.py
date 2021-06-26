import random

def roll_dice(throw_dice):
    shooting_sequence = [] #variable auxiliar

    for _ in range(throw_dice): #generar tantos tiros nos diga el parametro
        roll = random.choice([1, 2, 3, 4, 5, 6]) #esto es un tiro
        #random.randint(1, 7) otro metodo
        shooting_sequence.append(roll) 

    return shooting_sequence

def main(throw_dice, attempts_number):
    throw = [] #guardar todos los resultados aqui
    for _ in range(attempts_number):
        shooting_sequence = roll_dice(throw_dice) #numero de tiros a generar
        throw.append(shooting_sequence)

    throw_with_1 = 0
    for roll in throw:
        if 1 in roll: #verificar si hay 1 en la secuencia que lanzamos
            throw_with_1 += 1
        # if 1 not in roll:    
        #     throw_with_1 += 1

    probabilities_with_1 = throw_with_1 / attempts_number #calcular probabilidad
    print(f' Chance of getting 1 in {throw_dice} tosses = {probabilities_with_1} ')
    # print(f' Chance of getting not 1 in {throw_dice} tosses = {probabilities_with_1} ')

if __name__ == "__main__":
    throw_dice = int(input('How many times do you want to throw dice: '))
    attempts_number = int(input('How many times will the simulation run: '))

    main(throw_dice, attempts_number)
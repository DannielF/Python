#sacar la media con codigo
import random


def media(X): 
    return sum(X) / len(X)

if __name__ == "__main__":
    X = [random.randint(1, 20) for i in range(20)] #valores 1 al 20/ generar 20 valores
    µ = media(X) #mu(µ) media poblacion

    print(X)
    print(f'it´s media is: {µ}')
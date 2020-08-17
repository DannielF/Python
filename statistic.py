import random
import math

def media(X): #sacar la media
    return sum(X) / len(X)

def variance(X):
    mu = media(X)

    accumulator = 0 #guardar resultados sumatoria
    for x in X:
        accumulator += (x - mu)**2
    return round(accumulator / len(X), 4)

def standard_deviation(X):
    return round(math.sqrt (variance(X)), 4) #regresar raiz cuadrada varianza    

if __name__ == "__main__":
    X = [random.randint(1, 20) for i in range(20)] #valores 1 al 20/ generar 20 valores
    µ = media(X) #mu(µ) media poblacion
    Var = variance(X)  #Var de varianza
    σ = standard_deviation(X) #σ simbolo desviacion estandar

    print(f'The list is: {X}')
    print(f'Media is: {µ}')
    print(f'Variance is: {Var}')
    print(f'Standard deviation is: {σ}')
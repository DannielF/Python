def run():
    # for contador in range(1001):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
# imprimir los numeros pares de dos

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
#imprimir los numeros y detenerse en i

    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)
# empieza a escribir el texto y se detiene en la letra designada        


if __name__ == '__main__':
    run()
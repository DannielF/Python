def run():
    my_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3    
    }

    # print(my_diccionario['llave3'])
    # print(my_diccionario['llave1'])
    # print(my_diccionario['llave2'])

    poblacion_pais = {
        'Argentina': 4567890,
        'Brasil': 210456738,
        'Colombia': 50321567
    }

    # print(poblacion_pais['Brasil'])

    # for i in poblacion_pais.keys():
    #     print(i)

    # for i in poblacion_pais.values():
    #     print(i)

    for pais, poblacion  in poblacion_pais.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()
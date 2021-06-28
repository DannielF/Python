def personas_en_rango_edad(lista, minimo, maximo):
    for person in lista:
        age = person.get('edad')
        if age >= minimo and age <= maximo:
            print(f'Name : {person.get('nombres')} ')


lista = [
    {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "María", "apellidos": "Tristán Merchán", "edad": 20},
    {"nombres": "Tomas", "apellidos": "Tristán Merchán", "edad": 30},
    {"nombres": "Santiago", "apellidos": "Tristán Merchán", "edad": 40},
    {"nombres": "Andres", "apellidos": "Tristán Merchán", "edad": 80},
    {"nombres": "Magdalena", "apellidos": "Tristán Merchán", "edad": 50}


]

print(personas_en_rango_edad(lista, 50, 101))

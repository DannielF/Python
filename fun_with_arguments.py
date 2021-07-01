from pprint import pprint

# pprint -> pretty print
# Funcion con argumentos variables -> tupla *


def variable_argument(var1, *vari):
    pprint('Salidad: ' + str(var1))
    for var in vari:
        pprint(var)


variable_argument(2)
variable_argument(100, 90, 50)

# Funcion con argumentos variables -> diccionario **


def informar(**var):
    pprint(var)
    for key, value in var.items():
        pprint("%s == %s" % (key, value))


informar(name='poseidon', age=6000, city='Olimpo')

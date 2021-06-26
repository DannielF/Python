import random

def source_lineal(list, objective):
    match = False

    for element in list: #O(n) lineal
        if element == objective:
                match = True
                break
    return match

if __name__ == "__main__":
    size_list = int(input('What size do you want for the list: '))
    objective = int(input('What number do you want to find: '))

    list = [random.randint(0, 100) for i in range(size_list)]
    
    find = source_lineal(list, objective)
    print(list)
    print(f'The element {objective} {"is" if find else "no this"} in the list. ')
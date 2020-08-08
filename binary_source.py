#implementacion recursiva
import random

def binary_source(list, start, end, objective, iter_bin=0): 
    print(f'Find {objective} between {list[start]} and {list[end - 1]}')
    iter_bin += 1
    if start > end:
        return (False, iter_bin)
    middle = (end + start)// 2

    if list[middle] == objective:
        return (True, iter_bin)
    elif list[middle] < objective:
        return binary_source(list, middle + 1, end, objective, iter_bin=iter_bin)
    else:
        return binary_source(list, start, middle - 1, objective, iter_bin=iter_bin)        

if __name__ == "__main__":
    size_list = int(input('What size do you want for the list: '))
    objective = int(input('What number do you want to find: '))

    list = sorted([random.randint(0, 100) for i in range(size_list)])
    
    (find, iter_bin) = binary_source(list, 0, len(list), objective)
    print(list)
    print(f'The element {objective} {"is" if find else "no this"} in the list. ')
    print(f'Iter binary_source: {iter_bin}') #Cuantas iteraciones tomo hallar el resultado.
    #implementacion recursiva
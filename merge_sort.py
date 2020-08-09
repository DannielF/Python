# Ordenamiento por mezcla
import random

def merge_sort(list): # O(n log n) log lineal
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        print(left, '*' * 5, right) #ver como se separan las listas

        #llamada recursiva en cada mitad
        merge_sort(left)
        merge_sort(right)
        #iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #iterador para la lista principal
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1        

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print(f'left {left}, right {right}') 
        print(list)
        print('-' * 50)    
    return list            

if __name__ == "__main__":
    size_list = int(input('¿What size of list do you want? '))

    list = [random.randint(0, 100) for i in range(size_list)]
    print(list)
    print('-' * 20)

    sort_list = merge_sort(list)
    print(sort_list)

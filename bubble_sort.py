import random

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1): #O(n) * O(n) = O(n * n) = O(n**2) Cuadratica-polinomial
            if list [j] > list [j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

if __name__ == "__main__":
    size_list = int(input('¿What size do you want? '))

    list = [random.randint(0, 100) for i in range(size_list)]
    print(list)
    ordered_list = bubble_sort(list)
    print(ordered_list)
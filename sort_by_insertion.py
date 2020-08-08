import random

def sort_by_insertion(list):

    for indice in range(1, len(list)):
        current_value = list[indice]
        current_position = indice

        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1
        list[current_position] = current_value
    return list

if __name__ == "__main__":
    size_list = int(input('What size do you want for the list: '))
    list = [random.randint(0, 100) for i in range(size_list)]
    print(list)
    # print(len(list))
    sort_list = sort_by_insertion(list)
    print(sort_list)
# list1.append(1) Increase the index of the list

def show_quantity(list2):
    global list3, counter
    count_char = 0
    list3 = []
    counter = []
    index1 = 0
    for i in range(len(list2)):
        if list2[i] == list2[index1]:
            count_char += 1
        else:
            list3.append(list2[index1])
            counter.append(count_char)
            count_char = 1
        index1 = i

    return count_char


def print_data(v):
    for i in range(len(v)):
        print(v[i], end=' ')


def main():
    global list2
    list0 = input('')
    list1 = list0.replace(" ", "")
    list2 = list(list1)
    list2.append(1)
    show_quantity(list2)
    print_data(list3)
    print('\n')
    print_data(counter)


if __name__ == '__main__':
    main()

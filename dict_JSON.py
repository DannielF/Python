import json


def convert_json(entry1):
    global data1
    data1 = json.loads(entry1)
    return data1


def get_data(data1, dict1):
    global dict2
    dict2 = {}
    for key, value in dict1.items():
        for keyA, valueB in data1.items():
            if key == keyA:
                dict2[key] = valueB


def print_values(dict2):
    sumV = 0
    for value in dict2.values():
        sumV += value
    print(sumV)


def print_keys(dict2):
    for key in dict2.keys():
        print(key, end=(' '))


def main():
    convert_json(entry1)
    get_data(data1, dict1)
    print_values(dict2)
    print_keys(dict2)


if __name__ == '__main__':
    entry1 = input('')
    entry2 = input('')
    lista = list(entry2.split(" "))
    listb = (0, 0, 0, 0, 0, 0, 0)
    dict1 = dict([(k, v) for k, v in zip(lista, listb)])
    main()

#  {"Laravel": 6, "HTML": 2, "Flutter": 4, "IPOO": 3, "JavaScript": 4, "C#": 2, "TypeScript": 2}
#  JavaScript Vue Ionic HTML CSS

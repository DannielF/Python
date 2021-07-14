
def generos(l: list) -> list:
    '''  Returns a list without repeatings elements '''
    listB = []
    for i in range(len(l)):
        if l[i] in listB:
            None
        else:
            listB.append(l[i])


def album_que_no_tengo(ind: list, l: list, s: str) -> list:
    ''' Returns a list with the indices where word is in the list '''
    indexA = ind
    listA = l
    word = s
    listB = []
    for i in range(len(indexA)):
        if word in listA[indexA[i]]:
            listB.append(indexA[i])


def no_he_escuchado(l1: list, l2: list) -> list:
    ''' Return a list with the elements of the l1 that aren't in the l2 '''
    listA = l1
    listB = l2
    listC = []
    for i in range(len(listA)):
        if listA[i] in listB:
            None
        else:
            listC.append(listA[i])


def para_intercambiar(l1: list, l2: list) -> int:
    ''' Return a number of elements that can be exchanged '''
    listA = l1
    listB = l2
    to_change = 0
    for i in range(len(listA)):
        if listA[i] in listB:
            None
        else:
            to_change += 1
    print(to_change)

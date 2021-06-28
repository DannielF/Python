# data process
def add_north_south():
    global count_north
    count_north = 0
    count_south = 0
    for ele in option_citizen:
        if ele in north_team:
            count_north += 1
        if ele in south_team:
            count_south += 1
        if count_north > count_south:
            print('N', end='')
        if count_south > count_north:
            print('S', end='')
        if count_north == count_south:
            print('E', end='')
    return count_north, count_south

# data entry


def data_entry():
    global north_team, south_team, option_citizen
    north_team = list(input('Vacunas equipo norte: '))
    south_team = list(input('Vacunas equipo sur: '))
    option_citizen = list(input('Vacuna de los ciudadanos: '))


def main():
    data_entry()
    add_north_south()


if __name__ == '__main__':
    main()

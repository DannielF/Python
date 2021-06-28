from typing import Any


def calc_pfizer(aztrazeneca: int) -> int:
    global pfizer
    pfizer = (aztrazeneca * 2) + 4
    return pfizer


def calc_janseen(aztrazeneca: int, pfizer: int) -> int:
    global janssen
    janssen = int((aztrazeneca + pfizer) / 5)
    return janssen


def phase_vaccination(jassen: int) -> str:
    if janssen <= 20:
        print("uno")
    elif janssen >= 21 and janssen < 31:
        print("dos")
    elif janssen >= 31 and janssen < 51:
        print("tres")
    elif janssen >= 51:
        print("cuatro")
    else:
        print("error")


def main():
    aztrazeneca: int = int(input('Cantidad de dosis Aztrazeneca: '))
    calc_pfizer(aztrazeneca)
    calc_janseen(aztrazeneca, pfizer)
    print(aztrazeneca, end=' ')
    print(calc_pfizer(aztrazeneca), end=' ')
    print(calc_janseen(aztrazeneca, pfizer))
    phase_vaccination(janssen)


aztrazeneca: int = 0
pfizer: int = 0
janssen: int = 0

if __name__ == "__main__":
    main()

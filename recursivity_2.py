""" def print_numbers(n):
    number = 0
    if n == 0:
        return 0
    else:
        print_numbers(n-1)
        number += n
        print(number)


print_numbers(5) """


""" def greeting(n):
    if n > 0:
        greeting(n-1)
        print(f'Hello #. {n}')


greeting(5) """


""" def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n-1)


print(f'The sum is: {sum_numbers(5)}') """


""" def max(a, b):
    mayor = a
    if b > mayor:
        mayor = b
    return mayor


def max3(a, b, c):
    return max(a, max(b, c))


def main():
    x = 8
    y = 25
    z = 10
    print(max(x, y))
    print(max3(x, y, z))


main() """


""" def sum_2(n):
    if n == 0:
        return 0
    else:
        result = sum_2(n-1)
        sum = n + result
        return sum


print(f'The sum is: {sum_2(5)}')
 """


# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2    - 2 * 1
# factorial(3) = 6    - 3 * 2 * 1
# factorial(4) = 24    - 4 * 3 * 2 * 1


""" def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


factorial(50) """

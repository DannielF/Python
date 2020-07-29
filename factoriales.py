
def factorial(n):
    '''Calcula el factorial de n.
        n int > 0
        return n!
    '''
    print(n)
    if n == 1:
        return 1
    return n * factorial(n -1)

n = int(input('Write a whole number: '))  

print(factorial(n))

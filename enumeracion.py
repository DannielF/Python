objetive = int(input('Choose a whole number: '))
answer = 0

while answer**2 < objetive:
    answer += 1

if answer**2 == objetive:
    print(f'Square root of {objetive} is {answer}')

else:
    print(f'{objetive} it doesn´t have square root exact')
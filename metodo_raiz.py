def run ():
    chooise = '''
    Welcome to methods of square root: 🐱‍👤

    1 - method enumeration
    2 - method approach
    3 - method binary search

    Choise an option: '''

    option = int(input(chooise))

    if option == 1:
        objetive = int(input('Choose a whole number: '))
        answer = 0
        while answer**2 < objetive:
            answer += 1
        if answer**2 == objetive:
            print(f'Square root of {objetive} is {answer}')
        else:
            print(f'{objetive} it doesn´t have square root exact')

    if option == 2:
        objective = int(input('Choose a number: '))
        epsilon = 0.01
        step = epsilon**2
        answer = 0.0
        while abs(answer**2 - objective) >= epsilon and answer <= objective:
            # print(abs(answer**2 - objective), answer)
            answer += step
        if abs(answer**2 - objective) >= epsilon:
            print(f'Square root of {objective} not found')
        else:
            print(f'Square root of {objective} is {answer}')
                
    if option == 3:
        objective = int(input('Choose a number: '))
        epsilon = 0.01
        low = 0.0
        high = max(1.0, objective)
        answer = (low + high) / 2
        while abs(answer**2 - objective) >= epsilon:
            # print(f'low={low}, high={high}, answer={answer}')
            if answer**2 < objective:
                low = answer
            else:
                high = answer
            answer = (high + low) / 2
        print(f'Square root of {objective} is {answer}')
        
    else:
        print('Write a right option: ')
        
if __name__ == '__main__':
    run()
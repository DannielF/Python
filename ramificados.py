def run():
    name_1 = str(input('What is your name: '))
    age_1 = int(input('How old are you: '))
    print(f'Your name is {name_1} and your age is {age_1}')
    name_2 = str(input('What´s your friend´s name: ')) 
    age_2 = int(input('How old is he: '))
    print(f'his name is {name_2} and his age is {age_2}')

    if age_1 > age_2:
        print(f'{name_1} are older than {name_2}')
    elif age_1 < age_2:
        print(f'{name_2} is older than {name_1}')
    elif age_1 == age_2:
        print('both of you have the same age')
    else:
        print('wrong way')            
if __name__ == '__main__':
    run()    

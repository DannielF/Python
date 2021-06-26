import random

def create_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F']
    minus = ['a', 'b', 'c', 'd', 'e', 'f']
    symbols = ['+', '=', '#', '!']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

    characters = mayus + minus + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = ''.join (password)
    return password    



def run():
    password = create_password()
    print('Your new password is: ' + password)

if __name__ == '__main__':
    run()
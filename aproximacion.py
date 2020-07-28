objective = int(input('Choose a number: '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    print(abs(answer**2 - objective), answer)
    answer += step

if abs(answer**2 - objective) >= epsilon:
    print(f'Square root of {objective} not found')
else:
    print(f'Square root of {objective} is {answer}')
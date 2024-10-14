import random

print('Guess the number!')

name = input('What is your name?: ')
print(f'Ok {name}, I have thought of a number between 1 and 100, '
      f'and you only have eight attempts to guess what the number is. Are you ready?')

answer = random.randrange(1, 100, 1)

for i in range(8):

    number = int(input('Enter a number: '))

    if number < 1 or number > 100:
        print('Invalid number')

    elif number < answer:
        print('Incorrect answer. The correct number is higher.')

    elif number > answer:
        print('Incorrect answer. The correct number is lower.')

    elif number == answer:
        print('You win!!')
        print(f'You took {i+1} attempts to find the correct number.')
        exit()

    else:
        print('You do not find the correct number in the 8 attempts.')

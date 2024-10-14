print('Welcome to the comision calculator!')

name = input('What is your name?: ')
sales = int(input('How much in sales did you make this month?: '))
commissions = int(input('What is your commission rate? (enter as %): '))

earnings = sales * commissions / 100

print(f'Hello {name}! Your comisions this month are ${earnings:.2f}')

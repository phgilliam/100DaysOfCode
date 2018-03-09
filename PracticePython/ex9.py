import random

x = random.randint(1,9)
guess = 0
inp = 0
while inp != 'e':
    inp = input('Enter a number between 1 and 9 or \'e\' to exit: ')
    try:
        if inp == 'e':
            break
        elif int(inp) < x:
            print('Too Low')
        elif int(inp) > x:
            print('Too High')
        elif int(inp) == x:
            print('Nailed it')
            break
        else:
            print('That is not an accepted value')
    except ValueError:
        print('not an accepted value')

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
            guess += 1
            print('Too Low, You\'ve made ' + str(guess) + ' guesses')
        elif int(inp) > x:
            guess += 1
            print('Too High, You\'ve made ' + str(guess) + ' guesses')
        elif int(inp) == x:
            guess += 1
            print('Nailed it in ' + str(guess) + ' guesses')
            break
        else:
            print('That is not an accepted value')
    except ValueError:
        print('not an accepted value')

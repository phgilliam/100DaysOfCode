import random

def comp_rps():
    seq = ['r','p','s']
    return str(random.choice(seq))

def game(comp,play):
    if play == 'r' and comp == 's':
        return 'Player Wins!'
    elif play == 'p' and comp == 'r':
        return 'Player Wins!'
    elif play == 's' and comp == 'p':
        return 'Player Wins!'
    elif play == 'q':
        return 'Thanks for playing!'
    elif play != 'r' or play != 'p' or play != 's' or play != 'q':
        return 'Enter \'r\',\'p\',\'s\' or \'q\''
    else:
        return 'Computer Wins'



x = input('Type \'q\' to quit, press anything to continue: ')
while x != 'q':
    x = input('\'r\' for rock, \'p\' for paper \'s\' for scissors: ')
    y = comp_rps()
    print(game(y,x))




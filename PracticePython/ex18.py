import random

x = random.randint(0,9999)

def cow_bull(c,u):
        bull = 0
        cow = 0
        
        for x in str(c):
                if x in str(u):
                        cow += 1

        for x,y in zip(str(c),str(u)):
                if x == y:
                        bull += 1

        return str(bull) + ' bull(s) and ' + str(cow) + ' cow(s)'

while True:
        y = input('guess:  ')
        print(cow_bull(x,y))

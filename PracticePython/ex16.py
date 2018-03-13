import random

lines = [line.rstrip('\n') for line in open('engmix.txt')]
a = random.randint(0,84099)
b = random.randint(0,84099)
c = random.randint(1,1000)

def wonky(a):
        b = []
        for x in a:
                if random.choice([True,False]):
                        b.append(x.upper())
                else:
                        b.append(x)
        return ''.join(b)

d = ['!','@','#','$','%','*']
e = [wonky(lines[a]), wonky(lines[b]), str(c), random.choice(d)]

random.shuffle(e)

print(''.join(e))

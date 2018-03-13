import random

a = []

for x in range(10):
        x = random.randint(0,5)
        a.append(x)

b = set(a)

print(a)
print(b)

c = []

for x in a:
        if x not in c:
                c.append(x)

print(c)

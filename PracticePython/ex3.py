import random

def genList(length, maximum):
    a = []
    for x in range(0,length):
        b = random.randint(1,maximum)
        a.append(b)
    return a

arr = genList(10,15)

while True:
    try:
        limit = input('Clean out numbers above what point? ')
        limit = int(limit)
    except ValueError:
        print('Please enter an integer')
        continue
    else:
        break
newList = list(filter(lambda x: x < limit, arr))
print(arr)
print(newList)

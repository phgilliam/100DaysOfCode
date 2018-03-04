import random

def genList(length,maximum):
    a = []
    for x in range(0,length):
        b = random.randint(1,maximum)
        a.append(b)
    return a

arr1 = genList(10,15)
arr2 = genList(15,10)

def listOverlap(a, b):
    arr = []
    for x in a:
        if x not in arr:
            if x in b:
                arr.append(x)
    return arr

print(arr1)
print(arr2)
print(listOverlap(arr1,arr2))

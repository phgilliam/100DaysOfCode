def factor(num):
    li = []
    x = range(1,num)
    for y in x:
        if num % y == 0:
            li.append(y)
    return li

def prime(num):
    if factor(num) == [1]:
        return True
    elif num == 1:
        return False
    else:
        return False


print(prime(1))
print(prime(13))
print(prime(12))

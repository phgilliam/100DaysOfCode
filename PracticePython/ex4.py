def factor(num):
    li = []
    x = range(1,num+1)
    for y in x:
        if num  % y == 0:
            li.append(y)
    return li

print(factor(100))

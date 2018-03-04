def factor(num):
    li = []
    x = range(1,num+1)
    for y in x:
        if num  % y == 0:
            li.append(y)
    return li

print(factor(100))

while True:
    try:
        x = input('Enter a number to factor: ')
        x = int(x)
    except ValueError:
        print('Please enter an integer!')
        continue
    else:
        break


print(factor(x))

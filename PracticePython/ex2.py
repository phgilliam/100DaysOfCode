def multipleOf(num, check):
    mod = num % check
    check = str(check)
    if(mod == 0):
        result = 'Your number is a multiple of ' + check
    else:
        result = 'Your number is not a multiple of ' + check
    return result 
while True:
    try:
        num = int(input('What number are we checking? '))
        check = int(input('We\'re checking ' + str(num) + ' for multiples of ... '))
    except ValueError:
        print('That is not a valid entry')
        continue
    else:
        break
print(multipleOf(num, check))

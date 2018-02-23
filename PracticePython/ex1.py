##Add input type checking
##Collect Birthday (mm/dd/yyyy) and tell them what day their birthday falls on in 100 years
##Add insults based on age for wrong inputs


def hundred(name, age, bd):
    if(bd.lower() == 'y'):
        year = 2018
    else:
        year = 2017
    fromNow = year - age + 100
    greeting = 'Hey, ' + name + ' you\'ll turn 100 in the year ' + str(fromNow)
    return greeting

name = input('Hey! What\'s your name? ')
age = input('Hey, ' + name + '! How old are you!? ')
age = int(age)
bd = input('Hey ' + name + ', have you had your birthday yet? (Y/N)')
num = input('Enter a number just for fun')
num = int(num)

def fun(num):
    output = ''
    for x in range(0,num):
        output += hundred(name, age, bd) + '\n'
    return output

print(fun(num))

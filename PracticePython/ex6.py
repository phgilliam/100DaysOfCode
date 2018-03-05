def palindrome(string):
    arr = []
    for x in string:
        arr.insert(0,x)
    pal = ''.join(str(x) for x in arr)
    if pal == string:
        return True
    else:
        return False

print(palindrome('test'))
print(palindrome('anna'))

x = input('Check if the word is a palindrome: ')

if palindrome(x) == True:
    print('Yep that\'s a palindrome!')
else:
    print('nope, sorry!')
    

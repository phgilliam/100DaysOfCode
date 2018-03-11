a = [5,10,15,20,25,30]
b = [25]
def first_and_last(l):
    b = []
    if len(l) >= 2:
        b.append(l[0])
        b.append(l[-1])
        return b
    else:
        return 0


print(first_and_last(a))
print(first_and_last(b))       

x = int(input('Length of list of Fibonacci numbers: '))

fib = [int((((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/5**0.5) for n in range(x)]

print(fib)

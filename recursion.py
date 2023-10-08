def factorial(n):
     return 1 if(n == 1) else n * factorial(n-1)
print(factorial(5))


mlist = range(1,10)
print(len(list(mlist)))
import functools

num = [1,2,3,4,5]

print("The sum of all the elements is: ", end="")
print(functools.reduce(lambda x,y: x+y,num))

result = functools.reduce(lambda a,b: a if a>b else b, num)
print(result)
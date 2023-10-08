nums = [1,2,3,4]

def gen(n):
    for i in n:
        yield  i

ob1 = gen(nums)

print(next(ob1))
print(next(ob1))
print(next(ob1))


str = "rume"
iter1 = iter(str)

print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))


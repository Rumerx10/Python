def myFun(n):
    vowels = ['a','e','i','o','u']
    if n in vowels:
        return True
    else : return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = list(filter(myFun, sequence))
print(filtered)

for x in filtered:
    print(x)
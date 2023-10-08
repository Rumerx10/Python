# Unpacking _______________
def fun(a, b, c):
    print(a, b, c)
abc = [1, 3, 5]
fun(*abc)

def rng(a, b):
    print(list(range(a,b)))
ft = [1,5]
rng(*ft)

# Packing _______________

def myf(*args):
    print(args)
myf(1,2,3)

def myD(**kwargs):
    print(f"My first name is: {kwargs['fname']} and my last name is: {kwargs['lname']} ")
myD(fname="Hasan",lname="Rume")
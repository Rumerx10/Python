# mypairs = [(1,2),(3,4),(5,6)]
# for p1,p2 in mypairs:
#     print(p1)
#     print(p2)
#
# i = 1
# while i<5:
#     print("i is: {}".format(i))
#     i += 1
#
# for i in range(6,10):
#     print(i)
#
# digits = [1,2,3,4,5,6,7,8,9,10]
# for i in range(5):
#     print("Digits: ", digits[i])
#
#
# out = [i**2 for i in digits]
# print(out)

# def my_func(param1='default'):
#     print("my function with param1 as: {}".format(param1))
#
# my_func()
#
# def hello():
#     return "Hello"
#
# print(hello())
#
# myList = [1,2,3,4,5,6,7,8,9,10]
#
# newList = list(filter(lambda a: a%2==0,myList))
# print(newList)

class Animal:
    def __init__(self):
        print('Animal Created')
    def whoAmI(self):
        print('Animal')
    def eat(self):
        print('Eating')

class Cow(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cow created')



mya = Cow()
mya.whoAmI()
mya.eat()


# a,b,c = input().split()
# a,b,c = [int(x) for x in [a,b,c]]
#
# g = max(a,b,c)
# print(g)
import math
# x1,y1 = list(map(float, input().split()))
# x2,y2 = list(map(float, input().split()))
# distance = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
# print("%.4f" % distance)
# n = 11257
# if n>0 and n<1000000:
#     while n>0:
#         print(n)
#         if(n>=100):
#             hundred = math.floor(n / 100)
#             print(hundred," nota(s) de R$ 100,00")
#             n = n-hundred*100
#             if (n < 50): print(0, " nota(s) de R$ 50,00")
#         if(n>=50):
#             fifty = math.floor(n/50)
#             print(fifty," nota(s) de R$ 50,00")
#             n = n - fifty * 50
#             if (n < 20): print(0, " nota(s) de R$ 20,00")
#         if(n>=20):
#             twenty = math.floor(n/20)
#             print(twenty, " nota(s) de R$ 20,00")
#             n = n - twenty * 20
#             if(n<10): print(0, " nota(s) de R$ 10,00")
#         if (n >= 10):
#             ten = math.floor(n/10)
#             print(ten, " nota(s) de R$ 10,00")
#             n = n - ten * 10
#             if (n < 5): print(0, " nota(s) de R$ 5,00")
#         if (n >= 5):
#             five = math.floor(n / 5)
#             print(five, " nota(s) de R$ 5,00")
#             n = n - five * 5
#             if (n < 2): print(0, " nota(s) de R$ 2,00")
#         if (n >= 2):
#             two = math.floor(n / 2)
#             print(two, " nota(s) de R$ 2,00")
#             n = n - two * 2
#             if (n < 1): print(0, " nota(s) de R$ 1,00")
#         if(n>=1):
#             one = math.floor(n/1)
#             print(one, " nota(s) de R$ 1,00")
#             n = n - one * 1

# a = [100, 50, 20, 10, 5, 2, 1]
# print(n)
# for x in a:
#     if (n >= x):
#         notes = math.floor(n / x)
#         print(notes, " nota(s) de R$ %d,00" %x)
#         n = n - notes * x
#     else: print(0, " nota(s) de R$ %d,00" %x)
#


# s = 140153
# h = math.floor(s/3600)
# s = s - (h*3600)
# m = math.floor(s/60)
# s = math.floor(s - m*60)
#
# print("%d:%d:%d" %(h,m,s))

# import math
# days = 400
# year = math.floor(days/365)
# days = (days - year*365)
# month = math.floor(days/30)
# days = math.floor(days-month*30)
# print(year)
# print(month)
# print(days)

# class MyMeta(type):
#     pass
# class MyClass(metaclass=MyMeta):
#     pass
# class MySubClass(MyClass):
#     pass
# print(type(MyMeta))
# print(type(MyClass))
# print(type(MySubClass))
#______________________________Named Tuple___________________
# from collections import namedtuple
# Color = namedtuple("Color",['red','green','blue'])
# color = Color(red=55,blue= 155,green= 255)
#
# print(color.blue)# will print according to name
# print(color[1])# will print according to Color d index number

# from my_modules import *
#
# fname()
# lname()
# nickname()
#
#
# x = lambda a : a*10
# print(x(5))

# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%d %B %Y"))


def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


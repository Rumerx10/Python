n = [1,2,3,4,5]

# def double_even_nums(p):
#     if p % 2 == 0 : return p*2
#     else: return p

# result = list(map(double_even_num,n))

result = list(map(lambda x: x*2, n))
print(result)

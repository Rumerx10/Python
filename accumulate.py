import functools
import itertools

nums = [1, 2, 6, 4, 3, 7, 8]
iter_result = itertools.accumulate(nums, lambda a,b: a+b)
print(list(iter_result))


reduce_result = functools.reduce(lambda a,b : a+b,nums)
print(reduce_result)
